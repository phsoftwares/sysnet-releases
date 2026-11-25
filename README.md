# SYSNET Releases

Repositório público para distribuir versões do SYSNET. Mantenha aqui somente manifestos e assets de Release; os fontes ficam nos repositórios privados. Não coloque tokens, configurações de clientes ou chaves privadas neste repositório.

## Downloads

Baixe a versão estável de cada componente. [Histórico de versões](https://github.com/phsoftwares/sysnet-releases/releases).

<!-- downloads:inicio -->
| Componente | Versão atual | Download |
| --- | --- | --- |
| Instalador | 11.3 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/sysnet-installer-v11.3-2026.5.19/SysNet-Instalador-v11.3.exe) |
| Gerencial | 2026.5.21 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/gerencial-v2026.5.21/Sys_Net_Gerencial.zip) |
| PDV | 2026.5.21 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/pdv-v2026.5.21/Sys_Net_NFCe.zip) |
| Servidor de integrações | 2026.5.19 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/server-v2026.5.19/Sys_Net_Server.zip) |
| Migrador Firebird → PostgreSQL | 2026.5.19 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/xfarma-migrador-v2026.5.19/XFarmaMigradorPostgres-2026.5.19.zip) |
| Backend | 2026.5.20 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/sysnet-backend-v2026.5.20/sysnet-backend-windows-amd64.zip) |
| Sync Agent | 2026.5.19 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/sysnet-sync-agent-v2026.5.19/sysnet-sync-agent-windows-amd64.zip) |
| Sync Backend | 2026.5.19 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/sysnet-sync-backend-v2026.5.19/sysnet-sync-backend-windows-amd64.zip) |
| Updater | 11.3.0 | [Baixar](https://github.com/phsoftwares/sysnet-releases/releases/download/sysnet-updater-v11.3.0/sysnet-updater-windows-amd64.zip) |
<!-- downloads:fim -->

## Gerencial, PDV e Server

O Gerencial consulta `channels/apps.json`. Publique primeiro uma Release com a tag e o asset indicados, depois atualize `version` e `tag` no manifesto. O Gerencial consulta o manifesto por HTTPS e baixa o ZIP da Release.

| Componente | Tag | Asset |
| --- | --- | --- |
| Gerencial | `gerencial-v<VERSAO>` | `Sys_Net_Gerencial.zip` |
| PDV | `pdv-v<VERSAO>` | `Sys_Net_NFCe.zip` |
| Server | `server-v<VERSAO>` | `Sys_Net_Server.zip` |

`channels/apps.json` é a única fonte de versão para Gerencial, PDV e Server. O Server usa a tag `server-v<VERSAO>` e o asset `Sys_Net_Server.zip`.

## Backend e sincronização

O `sysnet-updater` consulta `channels/stable.json` ou `channels/beta.json` para baixar `sysnet-backend`, `sysnet-sync-agent` e `sysnet-sync-backend`. O updater atual aceita JSON direto por HTTPS e valida sequência, validade, origem, tamanho e SHA-256 de cada ZIP; não exige assinatura Ed25519 nem certificado próprio. Envelopes assinados antigos continuam aceitos por compatibilidade, mas o novo canal beta de teste é JSON direto. O instalador continua usando `stable`; use `beta` somente em uma máquina/VM descartável.

Nunca publique os payloads de exemplo, os hashes ilustrativos ou a chave privada como canais válidos.
