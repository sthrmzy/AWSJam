# Passos para Atualizar o Bot no Amazon Lex

## 1. Acessando o Console do Amazon Lex
- Navegue até o **Amazon Lex Console**.
- No menu esquerdo, clique em **Bots**.

## 2. Selecionando o Bot
- Clique no bot chamado **PizzaPlace**.

## 3. Editando os Tipos de Slot
- No painel esquerdo, selecione **Tipos de Slot**.
- Clique no tipo de slot denominado **PizzaTypes**.
- Role para baixo até a seção **Valores do tipo de slot**.
- Adicione 3 novos valores de tipo de slot:
  - **Pizza Havaiana**
  - **Pizza de Almôndegas**
  - **Pizza de Fazenda**
- Clique em **Salvar** o tipo de slot.

## 4. Editando a Intenção de Pedido de Pizza
- No painel esquerdo, clique em **Intents**.
- Selecione a intenção chamada **OrderPizza**.
- Role para baixo até a seção de **slots**.
- Clique em **Prompt para WhichPizzaSlot**.
- Altere a mensagem de prompt para:  
  "Qual pizza você gostaria de pedir: Frango, Vegetariana, Pepperoni, Margherita, Havaiana, Almôndega, Fazenda?"
- Clique em **Salvar intenção**.

## 5. Criando e Testando o Bot
- Após salvar as alterações, crie o bot.
- Teste o bot para garantir que as alterações foram aplicadas corretamente.

