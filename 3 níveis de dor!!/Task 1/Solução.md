# Passo 1: Configurar o "Ouvinte" (Listener) do Application Load Balancer

## Problema Identificado

A mensagem de erro **"O grupo de destino não está configurado para receber tráfego do balanceador de carga"** indica que o ALB não sabe o que fazer com o tráfego que chega. Ele recebeu uma conexão da internet, mas não tem nenhuma regra para encaminhá-la ao grupo de destino (Target Group) onde estão as instâncias do WordPress.

## Justificativa da Solução

Um **"Ouvinte" (Listener)** é uma regra no Load Balancer que verifica as solicitações de conexão dos clientes. A regra mais básica é: **"Quando chegar tráfego na porta 80 (HTTP), encaminhe-o para este Grupo de Destino específico"**. Sem essa regra, o tráfego é descartado e o **Target Group** fica **"Não utilizado"** (Unused).

## Como Resolver

1. Acesse o **Console da AWS** e navegue até **EC2**.
2. No menu à esquerda, vá para **Balanceamento de Carga** (Load Balancing) -> **Load Balancers**.
3. Selecione o seu **Application Load Balancer**.
4. Clique na aba **Ouvintes** (Listeners).
5. Você provavelmente verá que não há nenhum ouvinte para a porta HTTP 80, ou ele está configurado incorretamente.
6. Clique em **Adicionar ouvinte** (Add listener).
7. Configure-o da seguinte forma:
   - **Protocolo : Porta** (Protocol : Port): **HTTP : 80**
   - **Ação padrão** (Default action): Selecione **Encaminhar para...** (Forward to...).
   - No campo do **Grupo de Destino** (Target Group), selecione o grupo que contém suas instâncias WordPress.
8. Clique em **Adicionar** (Add) ou **Salvar** (Save).

Ao final deste passo, o status do seu **Target Group** deve mudar de **"Unused"** para **"initial"** ou começar as verificações de saúde. Se as instâncias ainda não estiverem saudáveis (**"healthy"**), vamos para o próximo passo.
