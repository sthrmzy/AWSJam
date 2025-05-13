# Antecedentes

A primeira tarefa é criar uma função do **AWS Lambda** para usar programaticamente o recurso de **validação de políticas do IAM Access Analyzer**.

Você pode validar suas políticas usando as verificações de políticas do **AWS IAM Access Analyzer**. É possível criar ou editar uma política usando a **CLI da AWS**, a **API da AWS** ou o **editor de políticas JSON** no console do IAM.

O Access Analyzer valida sua política em relação à gramática e às **melhores práticas do IAM**. Você pode ver as **descobertas da verificação de validação de políticas**, que incluem:

- Avisos de segurança  
- Erros  
- Avisos gerais  
- Sugestões

Essas descobertas fornecem **recomendações práticas** que ajudam a criar políticas funcionais e em conformidade com as melhores práticas de segurança.

---

# Inventário

Você tem uma função Lambda chamada: `jam-validate-iam-policy-with-access-analyzer`

---

# Sua tarefa

Atualize a função do **AWS Lambda** `jam-validate-iam-policy-with-access-analyzer` para usar a capacidade de **validação de políticas** do IAM Access Analyzer.

---

# Por onde começar

1. No **Console de Gerenciamento da AWS**, acesse o console do **AWS Lambda**.
2. Revise o código-fonte da função Lambda `jam-validate-iam-policy-with-access-analyzer`.
3. Atualize o código para utilizar a chamada de API `ValidatePolicy` do IAM Access Analyzer.

✅ **O desafio será aprovado automaticamente quando você atualizar o código-fonte.**

