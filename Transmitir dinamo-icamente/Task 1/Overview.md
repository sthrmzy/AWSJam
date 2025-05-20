# 📄 Plano de Fundo

Os documentos deixados pelo desenvolvedor indicam que as duas tabelas do Amazon DynamoDB abaixo podem ser aproveitadas para atingir a meta comercial:

| Nome da Tabela     | Descrição                           |
|--------------------|-------------------------------------|
| CustTransactions   | Armazena todas as transações de clientes |
| CustProfile        | Armazena perfis de clientes         |

Na tabela **CustProfile**, o desenvolvedor adicionou dois campos adicionais para capturar:

- O gasto total de um cliente (`totalTNValue`)
- O status do cliente correspondente: `"Normal"` ou `"Elite"`

---

# 🧠 Contexto da Função Lambda

O desenvolvedor começou a trabalhar em uma função Lambda chamada:  JAM_Lambda_Exec_Function_EDIT_THIS


Essa função aceitará alterações na tabela **CustTransactions** como um evento e atualizará a tabela **CustProfile**.

Há um comentário no código `# SEU CÓDIGO VAI AQUI`, onde você precisa preencher os detalhes da lógica de atualização.

---

# ✅ Sua Tarefa

Concluir a função AWS Lambda para:

- Atualizar o **valor total das transações** do cliente (`totalTNValue`)
- Atualizar o **status do cliente** (`CustStatus`) na tabela **CustProfile**

Essa atualização deve ocorrer **sempre que o cliente fizer uma nova transação**.

---

# 🧪 Validação de Tarefa

Teste a função com o evento abaixo:

```json
{
   "Records": [
        {
            "eventName": "INSERT",
            "eventSource": "aws:dynamodb",
            "dynamodb": {
                "Keys": {
                    "CustID": {
                        "S": "task1test1record"
                    },
                    "TnValue": {
                        "N": "250"
                    }
                }
            }
        }
    ]
}

```

Após testar a função Lambda com sucesso, a verificação será feita automaticamente e a tarefa será marcada como concluída em alguns minutos.

# 📦 Inventário

🧠 Função Lambda

JAM_Lambda_Exec_Function_EDIT_THIS


🗃️  CustTransactions Table Schema:

Field	    Type	          Description
CustID	  string	  Unique identifier for customer
TnNum	    integer  	Unique identifier for transaction
TnValue	  integer	  Dollar value of transaction
-------------	-----------	--------------------------------


🗃️ CustProfile Table Schema:

Field	          Type	            Description
CustID	        string	    Unique identifier for customer
TotalTnValue	  integer	    Total Dollar value of all customer spend
CustStatus	    string	    Normal / Elite
-------------------	-----------	--------------------------

# ▶️ Começando
Acesse o console do AWS Lambda.

Se não visualizar a lista de funções:

Clique em Serviços no canto superior esquerdo

Escolha Lambda novamente para recarregar a lista

⚠️ Nota: A função de equipe do Jam pode ter restrições que impedem o acesso às funções de verificação automática.

🛠️ Serviços que Você Deve Usar
- AWS Lambda

 
