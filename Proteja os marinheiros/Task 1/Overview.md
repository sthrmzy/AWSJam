# Tarefa: Criar Tabela, Carregar Dados e Configurar Usuários no Redshift

Nesta tarefa, você criará uma tabela de marinheiros e carregará os dados. Além disso, você criará diferentes funções e usuários, conforme descrito no resumo do desafio.

Um data warehouse Redshift Serverelss (seabird-wg) foi pré-criado para você na conta.

## Etapa 1

Vá para o console Redshift. Expanda o painel de navegação esquerdo e clique em Editor de consultas V2.

Conecte-se ao armazenamento de dados do Redshift Server (seabird-wg) usando a opção “Nome de usuário e senha do banco de dados”.

- **username:** awsuser  
- **password:** Retrieve the password from RedshiftServerlessSecret-* secret in AWS Secrets Manager.  
- **database:** dev

## Etapa 2

Crie uma tabela sailors e carregue-a em `s3://redshift-demos/data/gamejam/sailors/` usando o comando COPY.

Consulte CREATE TABLE para obter a sintaxe. A seguir estão os nomes das colunas e os tipos de dados a serem usados.

s_id bigint,
s_name varchar(25),
s_address varchar(40),
s_phone varchar(15),
s_acctbal numeric(12,2),
s_segment varchar(10),
s_dietrestrictions varchar(20),
s_onboard boolean 

## Etapa 3

Crie usuários e funções abaixo.

Nomes de usuário: cook, cuddy, cashking  
Nomes dos papéis: capitão, tripulação, finanças

## Etapa 4

Conceder funções aos usuários.

- papel de capitão para usuário cozinheiro  
- Função crew para usuário cuddy  
- Papel de finance para usuário de sacar

---

### Qn: Quantos marinheiros embarcaram com status de diamante na viagem atual?
