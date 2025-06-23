# Atualizando o Bot PizzaPlace no Amazon Lex

## Contexto

A Pizzaria da Francesca foi renomeada para **Pizza Hot**, mas o bot de bate-papo ainda exibe o antigo nome **Pizzaria da Francesca**. Você precisará atualizar o bot para refletir a nova identidade **Pizza Hot** e ajustar os prompts de interação.

### Objetivo
- Alterar o nome no bot para **Pizza Hot** onde **Pizzaria da Francesca** for mencionado.
- Adicionar um novo tipo de slot para o **CrustTypes** para incluir as opções de crosta.
- Criar um novo prompt de slot para perguntar aos clientes sobre sua preferência de crosta.

---

## Passos para Atualizar o Bot

### 1. Acessando o Console do Amazon Lex
- Navegue até o **Amazon Lex Console**.
- No painel esquerdo, clique em **Bots**.

### 2. Selecionando o Bot
- Clique no bot chamado **PizzaPlace**.

### 3. Editando a Intenção de Pedido de Pizza
- No painel esquerdo, selecione **Intents**.
- Selecione a intenção chamada **OrderPizza**.

### 4. Atualizando o Nome para Pizza Hot
- No campo de **prompt** ou onde o nome da pizzaria é mencionado, substitua todas as ocorrências de **Pizzaria da Francesca** por **Pizza Hot**.

### 5. Adicionando um Novo Tipo de Slot para Crosta
- No painel esquerdo, clique em **Tipos de Slot**.
- Clique em **Criar Tipo de Slot**.
- Nomeie o tipo de slot como **CrustTypes** (sem espaços ou caracteres especiais).
- Adicione os seguintes valores ao tipo de slot:
  - **Fina**
  - **Regular**
- Clique em **Salvar**.

### 6. Adicionando o Novo Slot à Intenção
- Dentro da intenção **OrderPizza**, role para baixo até a seção de **slots**.
- Clique em **Adicionar Slot** e crie um novo slot com o nome **WhichCrust** (sem espaços ou caracteres especiais).
- Selecione o tipo de slot **CrustTypes**.
- Adicione um novo **prompt** para o slot **WhichCrust**:
  - **Mensagem do prompt**: "Qual crosta você gostaria de pedir, fina ou regular?"
  
### 7. Validação de Tarefas
- Após adicionar os valores de slot e criar os novos prompts, a tarefa será automaticamente validada para conclusão.
- Você pode clicar em **Check my Progress** para verificar o status da validação.

---

## Antes (Imagem de exemplo da interface do console do Amazon Lex)

![Antes](imagem_exemplo_antes.png)  

---

### 8. Testando o Bot
- Após salvar as alterações, crie e teste o bot.
- Verifique se o bot agora exibe o nome **Pizza Hot** em vez de **Pizzaria da Francesca** e se o novo prompt de crosta está funcionando corretamente.

---

## Serviços Envolvidos
- **Amazon Lex**: Para criar, editar e testar o bot.
- **Validação de Tarefas**: O sistema valida automaticamente se os slots e prompts foram configurados corretamente.

---

Após seguir esses passos, seu bot estará atualizado e pronto para interagir com os usuários com as novas opções de crosta e a marca correta, **Pizza Hot**.
