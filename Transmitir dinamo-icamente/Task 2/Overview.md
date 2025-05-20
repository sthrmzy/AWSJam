# Plano de Fundo

Parabéns! Você concluiu a função do **AWS Lambda**, que pode atualizar a tabela `CustProfile` no **Amazon DynamoDB** quase em tempo real sempre que o cliente fizer uma transação. No entanto, ainda não terminamos.

Em seguida, a função Lambda deve ser acionada automaticamente sempre que o cliente concluir uma nova transação para que o perfil do cliente possa ser atualizado imediatamente.

Quando conseguirmos isso, o status do perfil de um cliente será atualizado automaticamente para **Elite** ao fazer uma transação qualificada. Posteriormente, a equipe de front-end poderá então presentear o cliente com um novíssimo cartão de associado **Elite**, acompanhado de um convite para o evento exclusivo.

Você está entusiasmado com a perspectiva de contribuir para a satisfação do cliente e começar imediatamente a acionar a função Lambda sempre que um item for inserido na tabela `CustTransactions` do Amazon DynamoDB.

---

# Sua Tarefa

Você deve fazer as alterações necessárias para **acionar automaticamente a função AWS Lambda `Jam_Lambda_Exec_Function_Edit_This` sempre que um item for inserido na tabela `CustTransactions` do Amazon DynamoDB.**

---

# Validação de Tarefas

Depois de ativar a função Lambda para ser acionada quando um item for adicionado à tabela `CustTransactions` do DynamoDB, a verificação será concluída automaticamente e a tarefa será marcada como concluída.

> **Observação:** Com base nos parâmetros escolhidos, pode levar alguns minutos para que a função Lambda seja acionada e que o processo de verificação confirme a conclusão do desafio.

---

# Inventário

### **Função Lambda:**
- `Jam_Lambda_Exec_Function_Edit_This`

### **Esquema da tabela `CustTransactions`:**

| Campo   | Tipo     | Descrição                                 |
|---------|----------|--------------------------------------------|
| CustID  | string   | Identificador exclusivo para o cliente     |
| tnNum   | inteiro  | Identificador exclusivo para transação     |
| TNValue | inteiro  | Valor em dólares da transação              |

### **Esquema da tabela `CustProfile`:**

| Campo        | Tipo     | Descrição                                        |
|--------------|----------|--------------------------------------------------|
| CustID       | string   | Identificador exclusivo para o cliente           |
| totalTNValue | inteiro  | Valor total em dólares de todos os gastos do cliente |
| CustStatus   | string   | Normal / Elite                                   |

---

# Serviços e Recursos Que Você Deve Usar

- **AWS Lambda**
- **Streams do Amazon DynamoDB**
