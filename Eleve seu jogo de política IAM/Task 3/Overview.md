# 📘 Plano de Fundo

Agora, você tem uma função do **AWS Lambda** que avalia as **políticas do AWS IAM** usando o **IAM Access Analyzer** diariamente.

---

# 📦 Inventário

- Função Lambda: `jam-validate-iam-policy-with-access-analyzer`
- Regra de agendamento: **EventBridge**, criada na etapa anterior, executando a função diariamente.

---

# 🧩 Sua Tarefa

> Investigue e **corrija as descobertas** geradas pelo IAM Access Analyzer após a avaliação das políticas IAM.

✅ A tarefa será aprovada **automaticamente** quando **todas as descobertas forem resolvidas**.

---

# 🚀 Por Onde Começar

1. Acesse o **console do AWS Lambda**.
2. Localize e execute a função:  
   `jam-validate-iam-policy-with-access-analyzer`
3. Verifique a **saída da execução** (logs e resposta JSON).
4. Analise os **findings** (descobertas) retornados pelo Access Analyzer.
5. Para cada finding:
   - Leia a descrição.
   - **Edite a política IAM** correspondente no console do IAM.
   - Aplique **correções recomendadas** (sintaxe, permissões amplas, segurança).
6. Reexecute a função Lambda para validar se **não há mais descobertas**.

---

# ✅ Resultado Esperado

- A função Lambda executa sem retornar findings do IAM Access Analyzer.
- Todas as políticas IAM analisadas estão **corrigidas e em conformidade com boas práticas de segurança**.
