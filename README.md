# SYSNET Releases

Repositório público para distribuir versões do SYSNET. Mantenha aqui somente manifestos e assets de Release; os fontes ficam nos repositórios privados. Não coloque tokens, arquivos de configuração de clientes ou chaves privadas neste repositório.

## Gerencial, PDV e Servidor fiscal

O Gerencial da linha PostgreSQL consulta `channels/postgres-apps.json`. Para publicar um executável, crie primeiro uma Release com a tag e o asset indicados no manifesto. Depois atualize o campo `version` do componente. A aplicação consulta o arquivo por HTTPS e baixa os ZIPs anexados às Releases.

| Componente | Tag | Asset |
| --- | --- | --- |
| Gerencial | `gerencial-v<VERSAO>` | `Sys_Net_Gerencial.zip` |
| PDV | `pdv-v<VERSAO>` | `Sys_Net_NFCe.zip` |
| Servidor fiscal | `fnts-server-v<VERSAO>` | `Sys_Net_Server.zip` |

O manifesto inicial tem `components: {}`; isso deixa o canal ativo sem oferecer executáveis até a primeira publicação.

## Serviços Go

O `sysnet-updater` usa os canais assinados `channels/stable.json` e `channels/beta.json`. Cada envelope exige assinatura Ed25519 e hashes dos ZIPs. Esses canais só devem ser provisionados com uma chave de produção guardada fora deste repositório. Os exemplos com chave `demo-only` e URLs `EXEMPLO` não são Releases válidas e não devem ser publicados como canais.
