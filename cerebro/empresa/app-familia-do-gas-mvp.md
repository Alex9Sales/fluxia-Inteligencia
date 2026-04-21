# App Família do Gás - MVP

## Objetivo
Criar um aplicativo simples e inteligente para aumentar vendas, organizar clientes, acompanhar histórico de compra e ativar ações comerciais no momento certo.

## Problema principal
Hoje a operação perde vendas por falta de histórico organizado, pouca previsibilidade de recompra, reativação fraca e atendimento muito dependente de esforço manual.

## O que o app deve resolver
- guardar histórico de compra do cliente
- mostrar há quantos dias o cliente não compra
- organizar clientes por segmento
- apoiar campanhas de recompra e reativação
- facilitar atendimento e fechamento
- preparar base para agentes comerciais e automações

## Público principal
- operador comercial
- atendimento da Família do Gás
- gestão do negócio

## Resultado de negócio esperado
- mais recompra
- mais reativação
- mais previsibilidade comercial
- mais controle da base de clientes
- menos perda de venda por esquecimento

## MVP V1
O MVP deve ser simples, rápido e operacional.

### Funcionalidades principais
1. cadastro de clientes
2. histórico de compras por cliente
3. cálculo de dias desde a última compra
4. segmentação básica do cliente
5. lista de clientes para recompra
6. lista de clientes para reativação
7. registro de resultado de contato
8. visão rápida para o operador

## Estrutura de dados inicial

### Cliente
- nome
- telefone
- endereço
- bairro
- observações
- tem vasilhame reserva
- status
- data da última compra
- frequência estimada
- dias desde última compra

### Compra
- cliente
- data da compra
- produto
- quantidade
- valor
- forma de pagamento
- observações

### Ação comercial
- cliente
- tipo de ação
- data
- resultado
- observações
- responsável

## Segmentação inicial
- novo
- recorrente
- em atenção
- inativo
- reativado

## Telas do MVP

### 1. Dashboard
Deve mostrar:
- total de clientes
- clientes em recompra
- clientes inativos
- contatos pendentes
- vendas recuperadas

### 2. Clientes
Lista com:
- nome
- telefone
- bairro
- última compra
- dias sem comprar
- status

### 3. Perfil do cliente
Deve mostrar:
- dados principais
- histórico de compras
- histórico de contatos
- sugestão de próxima ação

### 4. Compras
Tela para registrar compras com rapidez.

### 5. Ações comerciais
Fila de clientes para:
- recompra
- reativação
- retorno

### 6. Resultado dos contatos
Registrar:
- vendeu
- interessado
- sem interesse
- sem resposta
- retornar depois

## Lógica comercial principal

### Recompra
Se o cliente está perto da frequência estimada, ele entra na fila de lembrete.

### Reativação
Se o cliente passou da janela normal, entra na fila de recuperação.

### Interesse detectado
Se o cliente demonstrar interesse, o sistema deve facilitar repasse rápido para fechamento.

## Papel dos agentes no futuro

### Agente de Recompra
Identifica clientes no momento ideal e sugere abordagem.

### Agente de Reativação
Encontra clientes parados e organiza contato comercial.

### Agente de Atendimento
Ajuda a responder, confirmar e fechar pedidos.

### Agente de Ligação
No futuro, pode ligar com script curto, qualificar interesse e registrar resultado.

## Fluxo ideal de operação
1. registrar compras
2. atualizar histórico do cliente
3. recalcular dias sem compra
4. alimentar fila comercial
5. executar contato
6. registrar resultado
7. fechar venda ou programar retorno

## Melhor forma de construir

### Fase 1
Painel simples com cadastro, histórico e fila comercial.

### Fase 2
Automação de mensagens e segmentação melhor.

### Fase 3
Agentes de IA e ligação assistida.

## Stack possível
- frontend web responsivo
- banco com Supabase
- backend leve com Node ou funções serverless
- integração futura com WhatsApp e automações

## Regra de produto
Não construir complexidade antes de validar rotina comercial real.

## Decisão executiva
O MVP deve nascer como sistema simples de operação comercial, não como plataforma pesada.

O foco é:
- vender mais
- lembrar na hora certa
- recuperar cliente parado
- organizar histórico
- preparar automação futura
