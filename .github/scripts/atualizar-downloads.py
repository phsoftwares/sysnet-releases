import json
import re
import subprocess
from pathlib import Path

REPOSITORIO = "phsoftwares/sysnet-releases"
README = Path("README.md")
INICIO = "<!-- downloads:inicio -->"
FIM = "<!-- downloads:fim -->"
VERSAO = r"[0-9]+(?:\.[0-9]+){0,2}"
APLICATIVOS = (
    ("gerencial", "Gerencial", "Sys_Net_Gerencial.zip"),
    ("pdv", "PDV", "Sys_Net_NFCe.zip"),
    ("server", "Servidor de integrações", "Sys_Net_Server.zip"),
)
SERVICOS = (
    ("sysnet-backend", "Backend"),
    ("sysnet-sync-agent", "Sync Agent"),
    ("sysnet-sync-backend", "Sync Backend"),
    ("sysnet-updater", "Updater"),
)


def releases_publicadas():
    resposta = subprocess.check_output(
        ["gh", "api", "--paginate", "--slurp",
         f"repos/{REPOSITORIO}/releases?per_page=100"],
        encoding="utf-8",
    )
    return {
        release["tag_name"]: release
        for pagina in json.loads(resposta)
        for release in pagina
        if not release["draft"] and not release["prerelease"]
    }


def componentes(canal):
    return json.loads(Path(f"channels/{canal}.json").read_text(encoding="utf-8-sig"))["components"]


def asset_da_release(releases, tag, nome):
    for asset in releases.get(tag, {}).get("assets", []):
        if asset["name"] == nome and asset["state"] == "uploaded":
            return asset["browser_download_url"]
    return None


def linha(componente, versao, url):
    return f"| {componente} | {versao} | [Baixar]({url}) |"


def mais_recente(releases, padrao, nome_asset, componente):
    disponiveis = []
    for tag in releases:
        match = re.fullmatch(padrao, tag)
        if match is None:
            continue
        versao = match.group("versao")
        url = asset_da_release(releases, tag, nome_asset.format(versao=versao))
        if url is not None:
            partes = tuple(map(int, versao.split(".")))
            ordem = partes + (0,) * (3 - len(partes))
            if "produto" in match.groupdict():
                ordem += tuple(map(int, match.group("produto").split(".")))
            disponiveis.append((ordem, versao, url))
    if not disponiveis:
        raise SystemExit(f"Nenhum pacote público encontrado para {componente}.")
    _, versao, url = max(disponiveis)
    return linha(componente, versao, url)


def tabela_downloads(releases):
    linhas = ["| Componente | Versão atual | Download |", "| --- | --- | --- |"]
    linhas.append(mais_recente(
        releases, rf"sysnet-installer-v(?P<versao>{VERSAO})-(?P<produto>[0-9]+\.[0-9]+\.[0-9]+)",
        "SysNet-Instalador-v{versao}.exe", "Instalador",
    ))
    apps = componentes("apps")
    stable = componentes("stable")
    for chave, componente, nome in APLICATIVOS:
        item = apps[chave]
        url = asset_da_release(releases, item["tag"], nome)
        if url is None:
            raise SystemExit(f"Pacote {nome} ausente na release {item['tag']}.")
        linhas.append(linha(componente, item["version"], url))
    linhas.append(mais_recente(
        releases, r"xfarma-migrador-v(?P<versao>[0-9]+\.[0-9]+\.[0-9]+)",
        "XFarmaMigradorPostgres-{versao}.zip", "Migrador Firebird → PostgreSQL",
    ))
    for chave, componente in SERVICOS:
        item = stable[chave]
        nome = item["url"].rsplit("/", 1)[-1]
        url = asset_da_release(releases, item["tag"], nome)
        if url != item["url"]:
            raise SystemExit(f"Pacote {nome} ausente ou divergente na release {item['tag']}.")
        linhas.append(linha(componente, item["version"], url))
    return "\n".join(linhas)


def main():
    conteudo = README.read_text(encoding="utf-8")
    if conteudo.count(INICIO) != 1 or conteudo.count(FIM) != 1:
        raise SystemExit("Marcadores de Downloads ausentes ou duplicados no README.")
    antes, depois = conteudo.split(INICIO)
    _, fim = depois.split(FIM)
    novo = f"{antes}{INICIO}\n{tabela_downloads(releases_publicadas())}\n{FIM}{fim}"
    if novo != conteudo:
        README.write_text(novo, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
