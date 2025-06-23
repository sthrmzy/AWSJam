# Alteração do Bot do Amazon Lex - Atualização dos Tipos de Pizza e Nome

## Fundo

A **Pizzaria da Francesca** agora é **Pizza Hot**, mas o bot de bate-papo ainda exibe o nome antigo "Pizzaria da Francesca". Você precisa alterar a configuração do bot para exibir **Pizza Hot** em vez de **Pizzaria da Francesca** e atualizar os tipos de pizza disponíveis no bot.

### Tipos de Pizza Atuais
- Pizza de Frango
- Pizza Vegetariana Delícia
- Pizza de Calabresa
- Pizza Margherita

### Novos Tipos de Pizza a Serem Adicionados
- Pizza Havaiana
- Pizza de Almôndegas
- Pizzaria da Fazenda

## Objetivo

1. **Alterar o nome** da pizzaria no bot para **Pizza Hot**.
2. **Adicionar novos tipos de pizza** ao bot, incluindo os novos tipos de pizza no slot de tipo de pizza, para que o bot aceite essas opções.

## Etapas para Realizar a Tarefa

### 1. Acesse o Console do Amazon Lex
- Navegue até o [**Console do Amazon Lex**](https://console.aws.amazon.com/lex).

### 2. Selecione o Bot
- No menu esquerdo, clique em **Bots**.
- Localize e clique no **Bot** chamado **PizzaPlace**.

### 3. Selecione a Intenção
- No menu à esquerda, clique em **Intents**.
- Encontre e clique na intenção chamada **OrderPizza**.

### 4. Modificar o Slot de Tipo de Pizza
- Role até a seção de **Slots**.
- Localize o slot que solicita o tipo de pizza. A consulta original do slot deve ser algo como:
  - **"Qual pizza você gostaria de pedir?"**.
- Alterar para algo como:
  - **"Qual pizza você gostaria de pedir: Frango, Vegetariana, Pepperoni, Margherita, Havaiana, Almôndega, Caseira?"**.
  
### 5. Adicionar Novos Tipos de Pizza ao Slot
- Adicione os novos tipos de pizza nos valores do **slot de tipo de pizza**:
  - **Pizza Havaiana**
  - **Pizza de Almôndegas**
  - **Pizzaria da Fazenda**
  
  Isso irá garantir que os novos tipos de pizza sejam aceitos pelo bot.

### 6. Alterar o Nome no Prompt da Intenção
- Localize o prompt onde o nome **Pizzaria da Francesca** é mencionado e altere para **Pizza Hot**.

#### Exemplo:

**ANTES:**
- **Valor do Slot:** Pizzaria da Francesca  
  ![Imagem Antes](link-para-imagem-antes) <!-- Substitua o link da imagem "ANTES" -->

**DEPOIS:**
- **Valor do Slot:** Pizza Hot  
  ![Imagem Depois](link-para-imagem-depois) <!-- Substitua o link da imagem "DEPOIS" -->

### 7. Salve a Intenção
- Após as alterações, clique em **Salvar intenção** para salvar as mudanças.

### 8. Criação e Teste do Bot
- Após salvar, crie o bot e faça os testes necessários para garantir que o nome foi alterado corretamente e que os novos tipos de pizza estão sendo aceitos.

---

## Validação de Tarefas
Assim que os valores forem atualizados, a tarefa será automaticamente validada para conclusão.

Você pode clicar em **Check my Progress** para verificar o status da tarefa e confirmar que a atualização foi concluída com sucesso.

---

## Serviços Envolvidos
- **Amazon Lex**: Usado para editar e atualizar o bot de bate-papo.

---

> **Dica**: Após as alterações, teste o bot com diferentes combinações de pizza para garantir que ele esteja respondendo corretamente a todos os novos tipos de pizza.

