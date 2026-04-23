# OmniRoute piloto

Objetivo: subir o OmniRoute de forma isolada para testar apenas:
- roteamento
- fallback
- health
- compatibilidade

Sem usar nesta fase:
- memory
- skills
- MCP
- A2A
- cloud sync
- integrações paralelas

## Arquivos
- `docker-compose.yml`
- `.env.example`
- `data/` será criada pelo container

## Recomendação
Subir no Coolify como Docker Compose.
Portainer também serve.

## Passo a passo

### 1. Criar stack/app
Use o conteúdo de `docker-compose.yml`.

### 2. Variáveis
Use `.env.example` como base e gere um `JWT_SECRET` forte.

### 3. Subir
Depois de subir, o esperado é:
- dashboard na porta `20128`
- API compatível na porta `20129`

## Depois que subir
No dashboard do OmniRoute, conectar apenas:
- OpenAI / ChatGPT
- Gemini

Não configurar agora:
- Claude
- Antigravity
- memory
- skills
- MCP
- A2A
- cloud sync

## Checklist de validação
Quando estiver no ar:
- container saudável
- dashboard abre
- endpoint `/v1/models` responde
- OpenAI conectado
- Gemini conectado
- fallback básico funcionando

## Observação importante
Este piloto não deve substituir o OpenClaw principal de imediato.
Primeiro validar o gateway isolado. Só depois decidir roteamento real.
