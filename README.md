# SYSNET Releases

Repositório público para distribuir versões do SYSNET. Mantenha aqui somente manifestos e assets de Release; os fontes ficam nos repositórios privados. Não coloque tokens, configurações de clientes ou chaves privadas neste repositório.

## Gerencial, PDV e Server

O Gerencial consulta `channels/apps.json`. Publique primeiro uma Release com a tag e o asset indicados, depois atualize `version` e `tag` no manifesto. O Gerencial consulta o manifesto por HTTPS e baixa o ZIP da Release.

| Componente | Tag | Asset |
| --- | --- | --- |
| Gerencial | `gerencial-v<VERSAO>` | `Sys_Net_Gerencial.zip` |
| PDV | `pdv-v<VERSAO>` | `Sys_Net_NFCe.zip` |
| Server | `server-v<VERSAO>` | `Sys_Net_Server.zip` |

`channels/apps.json` é a única fonte de versão para Gerencial, PDV e Server. O Server usa a tag `server-v<VERSAO>` e o asset `Sys_Net_Server.zip`.

## Backend e sincronização

O `sysnet-updater` consulta este mesmo repositório, pelos canais assinados `channels/stable.json` ou `channels/beta.json`, para baixar `sysnet-backend`, `sysnet-sync-agent` e `sysnet-sync-backend`. Esses canais usam envelopes assinados com Ed25519 e hashes dos ZIPs. A chave privada fica fora do repositório; clientes recebem apenas a chave pública confiável.

Nunca publique os payloads de exemplo, os hashes ilustrativos ou a chave privada como canais válidos.
