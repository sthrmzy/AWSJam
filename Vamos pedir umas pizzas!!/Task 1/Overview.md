# Alteração no Bot de Chat - De "Pizzaria da Francesca" para "Pizza Hot"

## Fundo

A **Pizzaria da Francesca** agora pertence à **Pizza Hot**, mas o bot de bate-papo ainda exibe o nome antigo "Pizzaria da Francesca". Sua tarefa é alterar a configuração do bot para exibir "Pizza Hot" sempre que o nome "Pizzaria da Francesca" for mencionado no chatbot.

## Sua Tarefa

Você deve editar o bot no **Amazon Lex** e fazer a seguinte alteração:

- Alterar o nome "Pizzaria da Francesca" para **Pizza Hot** no prompt da seção de intenções sempre que o nome da pizzaria for mencionado.

### Fluxo de Trabalho

1. **ANTES**: O bot atualmente usa o nome **Pizzaria da Francesca**.
    ![Imagem Antes](link-para-imagem-antes)  <!-- Substitua o link para a imagem antes -->

2. **DEPOIS**: Após as alterações, o bot irá exibir **Pizza Hot**.
    ![Imagem Depois](link-para-imagem-depois)  <!-- Substitua o link para a imagem depois -->

## Passos para Alteração

### 1. Acesse o Console do Amazon Lex

- Navegue até o **console do Amazon Lex** (console.aws.amazon.com/lex).
- Localize o bot **PizzaPlaceBot**.

### 2. Encontre a Intenção Correta

- No console, identifique a intenção chamada **OrderPizza** dentro do bot **PizzaPlaceBot**.
- Edite a intenção para fazer as modificações necessárias.

### 3. Modifique os Enunciados e Slots

- No editor da intenção **OrderPizza**, localize os enunciados que mencionam "Pizzaria da Francesca" e substitua-os por **Pizza Hot**.
- Verifique também os slots e outras configurações que possam conter o nome da pizzaria e atualize conforme necessário.

### 4. Ignorar Erros de Autorização

- Durante o processo, você pode ver erros de autorização no banner do console. **Ignore esses erros**, pois isso não afetará a tarefa de modificação do nome.

### 5. Validação de Tarefas

- Assim que as alterações forem feitas, a tarefa será automaticamente validada como concluída.
- Você também pode clicar no botão **Check my Progress** para verificar o status da sua tarefa.

---

## Serviços Envolvidos

- **Amazon Lex**: O serviço principal para modificar o bot de bate-papo.

---

> **Dica**: Lembre-se de testar o bot após as alterações para garantir que todas as instâncias do nome antigo foram corretamente substituídas.
