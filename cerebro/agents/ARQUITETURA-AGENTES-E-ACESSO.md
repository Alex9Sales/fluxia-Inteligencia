# Arquitetura de Agentes e Acesso

## Objetivo
Definir como Alex acessa Friday, Ayra e futuros agentes sem transformar a operação em bagunça.

Este documento organiza:
- hierarquia
- canais
- visibilidade
- governança
- fluxo entre agentes

## Regra central
Nem todo agente precisa falar diretamente com Alex.

A maioria dos agentes deve operar como camada especializada sob coordenação da Friday.

Friday continua sendo o centro de comando.

## Hierarquia
### 1. Alex
Dono do contexto, da direção e das decisões maiores.

### 2. Friday
CEO AI.
Camada principal de comando.
Responsável por:
- direção estratégica
- coordenação entre agentes
- revisão final
- decisões de priorização
- controle de qualidade

### 3. Agentes especialistas
Entram para executar funções específicas.

Exemplos:
- Ayra → Instagram e operação de conteúdo
- futuros agentes → vendas, atendimento, CRM, app, pesquisa, etc.

## Papel de cada camada
### Friday
- pensa o sistema
- define direção
- aprova
- orquestra
- protege coerência

### Agente especialista
- executa escopo específico
- não redefine direção sozinho
- entrega produção especializada
- reporta ou devolve para Friday quando necessário

## Como Alex deve acessar o sistema
### Canal principal
A conversa principal continua sendo com Friday em DM.

Esse é o canal executivo.

### Espaço operacional multiagente
Faz sentido criar um grupo de operação no Telegram.

Sugestões de nome:
- Fluxia AI Ops
- Mesa de Operações
- Friday Command
- Sales Tecnologia Ops

## Recomendação de estrutura no Telegram
### 1. DM com Friday
Usar para:
- decisões estratégicas
- direcionamento principal
- pedidos mais sensíveis
- síntese executiva

### 2. Grupo operacional
Usar para:
- execução multiagente
- acompanhamento de operação
- tarefas delegadas
- visibilidade de trabalho
- futuras interações entre agentes e Friday

## Como os agentes devem aparecer
### Regra recomendada
Agentes especialistas não devem falar o tempo todo.

Eles entram quando:
- forem acionados
- uma tarefa exigir especialidade
- Friday quiser expor um resultado de execução
- fizer sentido dar visibilidade ao trabalho daquele agente

## Modelo de presença
### Friday
Sempre presente como camada de comando.

### Ayra
Presença condicionada ao tema Instagram e conteúdo.

### Outros agentes
Entram só quando o escopo justificar.

## Como Friday e os agentes se relacionam
### Fluxo ideal
1. Alex pede ou direciona
2. Friday interpreta e decide quem entra
3. agente especialista executa
4. Friday revisa, sintetiza ou aprova
5. resultado volta para Alex

## Como Alex acompanha o que Ayra está fazendo
Há 3 níveis possíveis.

### Nível 1. Visão indireta
Friday mostra:
- pauta
- drafts
- revisões
- decisões

### Nível 2. Visão operacional
Ayra aparece no grupo operacional com entregas e atualizações visíveis.

### Nível 3. Canal dedicado
Ayra pode ter um canal ou sessão própria no futuro, se fizer sentido.

## Melhor escolha agora
### Curto prazo
- manter Friday como canal principal
- criar grupo operacional depois, com governança clara
- Ayra operar sob Friday

### Médio prazo
- grupo operacional multiagente
- agentes aparecem com escopo definido
- Friday continua como camada de comando

## O que evitar
- um monte de agentes falando ao mesmo tempo
- agentes com autoridade difusa
- duplicação de instrução
- conversas paralelas sem comando central
- especialista redefinindo estratégia sem passar por Friday

## Publicação e execução
No caso da Ayra, o fluxo fica:
- Ayra cria
- Friday aprova
- Ayra publica

No futuro, isso pode ganhar canal mais visível, mas a regra de governança não muda.

## Ferramentas por camada
### Friday
- segundo cérebro
- memória
- docs estratégicos
- revisão de saída
- coordenação geral

### Ayra
- docs de Instagram
- cronograma
- pauta
- OmniRoute para geração de texto
- futura camada de publicação quando o fluxo estiver estável

## Decisão prática atual
### Agora
- Friday segue como interface principal
- Ayra existe como agente especialista estruturada
- publicamente, a operação ainda é guiada por Friday

### Próxima expansão natural
- criar grupo operacional no Telegram
- definir quais agentes entram
- estabelecer regras de quem fala, quando e como

## Regra final
A operação multiagente só funciona se houver comando claro.

Nesse sistema, Friday é o eixo.
Os outros agentes aumentam capacidade.
Não substituem governança.
