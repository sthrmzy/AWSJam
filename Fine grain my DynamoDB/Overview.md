# Overview

Esse desafio ajudará o participante a entender o conceito de acesso refinado à tabela do DynamoDB.

## Introdução

### O que você aprenderá com esse desafio:

Neste desafio, você entende:

- Como fornecer acesso refinado em nível de item na tabela do DynamoDB  
- Como fornecer acesso refinado em nível de atributo na tabela do DynamoDB  

### Tópicos abordados

Ao resolver e superar esse desafio, você será capaz de:

- Editar uma política do IAM  
- Declaração de condição da política IAM  
- Usando as condições de `dynamodb:LeadingKeys`  
- Usando as condições de `dynamodb:Attri`

---

## Task 1

### Antecedentes

Cada item na tabela **GameScores** do Amazon DynamoDB é identificado exclusivamente por um ID de usuário e pelo nome do jogo que o usuário jogou. A tabela **GameScores** tem uma chave primária que consiste em uma chave de partição (`UserID`) e uma chave de classificação (`GameTitle`).  

Um usuário que deseja jogar um jogo deve pertencer a uma função do IAM chamada `game-users-role`, que tem uma política de segurança anexada a ela.

### Sua tarefa

Você precisa alterar a política anexada à função `game-users-role` e garantir que os usuários tenham **somente o acesso abaixo** na tabela do DynamoDB:

- `Get`, `Put` e `Update Items`  
- `Read/Write Items in batch`  
- `Delete Items`  
- `Query`

### Inventário

Os seguintes recursos foram fornecidos para que você possa enfrentar o desafio com sucesso:

- Tabela Amazon DynamoDB - `GameScores`  
- Função do AWS IAM - `game-users-role`  
- Política de IAM da AWS - `game-users-policy`

### Serviços que você deve usar

- Amazon DynamoDB

### ERA O OBJETIVO

### Começando

Acesse o console do IAM e edite a política anexada à função `game-users-role` e forneça somente as permissões necessárias.

### Validação de tarefas

A tarefa será automaticamente validada para conclusão.  
Como alternativa, você pode clicar em **Check my Progress** para verificar o status.

---

## Task 2

### Antecedentes

Agora você removeu todas as ações (`*`) para somente as ações selecionadas e precisamos limitar o acesso ao nível do item. Os usuários estão fazendo login usando suas credenciais da Amazon via federação de identidade da Web, e isso está sendo armazenado no atributo `userID` da tabela Amazon DynamoDB.

### Sua tarefa

Você precisa alterar a política anexada à função `game-users-role` para garantir que os usuários tenham acesso somente aos itens em que o valor da chave de partição corresponda ao ID do usuário.

### Inventário

- Tabela Amazon DynamoDB - `GameScores`  
- Função do AWS IAM - `game-users-role`  
- Política de IAM da AWS - `game-users-policy`

### Serviços que você deve usar

- Amazon DynamoDB

### ERA O OBJETIVO

### Começando

Acesse o console do IAM e edite a política anexada à função `game-users-role` e forneça as chaves de condição necessárias.

### Validação de tarefas

A tarefa será automaticamente validada para conclusão.  
Como alternativa, você pode clicar em **Check my Progress** para verificar o status.

---

## Task 3

### Antecedentes

Agora você removeu todas as ações (`*`) para somente as ações selecionadas e forneceu limitação de acesso ao nível do item. Você também precisa fornecer acesso em nível de atributo.

### Sua tarefa

Você precisa alterar a política anexada à função `game-users-role` para limitar o acesso a **somente os atributos abaixo**:

- ID de usuário  
- Título do jogo  
- Vitórias  
- Perdas  
- Pontuação máxima  
- Data e hora da melhor pontuação  

Também deve garantir que o aplicativo:

- Sempre forneça uma lista de atributos específicos sobre os quais agir  
- **Não pode solicitar todos os atributos**

### Inventário

- Tabela Amazon DynamoDB - `GameScores`  
- Função do AWS IAM - `game-users-role`  
- Política de IAM da AWS - `game-users-policy`

### Serviços que você deve usar

- Amazon DynamoDB

### ERA O OBJETIVO

### Começando

Acesse o console do IAM e edite a política anexada à função `game-users-role` e modifique as chaves de condição necessárias.

### Validação de tarefas

A tarefa será automaticamente validada para conclusão.  
Como alternativa, você pode clicar em **Check my Progress** para verificar o status.
