# Plano de Fundo

Agora você tem uma **função do AWS Lambda** capaz de **avaliar as políticas do IAM** usando o **IAM Access Analyzer**.  
Você deseja executar essa função **periodicamente**, para garantir que políticas IAM **novas ou atualizadas** sejam avaliadas regularmente.

---

# Inventário

Você tem a seguinte função Lambda: `jam-validate-iam-policy-with-access-analyzer`


# Sua Tarefa

Anexe um **gatilho** à função Lambda para que ela seja **executada diariamente**.

---

# Por Onde Começar

- Acesse o **Console do AWS Lambda**.
- Explore a seção **Triggers** (gatilhos).
- Adicione um **evento programado** do **Amazon EventBridge (antigo CloudWatch Events)** para acionar a função **uma vez por dia**.

✅ **O desafio será validado automaticamente** quando o gatilho correto for anexado.


