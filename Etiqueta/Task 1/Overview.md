# Desafio IAM - Controle de Acesso por Tag para EC2

## 📘 Plano de Fundo

Você é o **administrador do IAM** para suas contas da AWS. Existem dois projetos, **Vermelho** e **Verde**, que estão executando e gerenciando instâncias do EC2 na **mesma conta da AWS**.

### Recursos Existentes

- **Funções do IAM:**
  - `ProjectRedRole` com tag: `Project = Vermelho`
  - `ProjectGreenRole` com tag: `Project = Verde`

- **Instâncias do EC2:**
  - Instância Vermelha com tag: `Project = Vermelho`
  - Instância Verde com tag: `Project = Verde`

- **Política Gerenciada Existente:**
  - `ManageEC2InstancesWithProjectTag`
  - Atualmente **excessivamente permissiva** e **sem condições de IAM** aplicadas.

---

## ✅ Requisitos

Você deve **editar a política IAM existente** para atender aos seguintes **três requisitos**:

### 1. Restringir Start/Stop

Permitir as ações `ec2:StartInstances` e `ec2:StopInstances` **somente** se a instância EC2 tiver uma tag `Project` cujo valor corresponda ao da função que está realizando a ação:

- `ProjectRedRole` → somente em instâncias com `Project = Vermelho`
- `ProjectGreenRole` → somente em instâncias com `Project = Verde`

### 2. Permitir RunInstances com Tags Corretas

Permitir `ec2:RunInstances` **somente se**:

- As **instâncias** e os **volumes** forem criados com uma **tag `Project`** com **valores que correspondem exatamente** (case-sensitive) ao da função.
- Nenhuma outra chave de tag além de `Project` seja usada.

### 3. Impedir Alteração de Tags

Impedir ações que **modifiquem tags** após a criação:

- Instâncias EC2
- Volumes EC2

---

## 🧪 Testes

1. Salve suas alterações na política.
2. Aguarde **20 segundos**.
3. Navegue até ou atualize a página referenciada por `VerifierURI` nas **propriedades de saída**.
4. Os **resultados dos testes** serão exibidos:
   - ✅ Verde = Teste passou
   - ❌ Vermelho = Teste falhou
5. Quando **todos os testes passarem**, você verá a **Resposta do Desafio** ao final da página.

---

## 🔗 Links Úteis

- [Ações, Recursos e Chaves de Condição para Amazon EC2](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html)
- [Chaves de Condição de Contexto Global da AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)
- [Exemplo: Usar Tags para Controlar o Lançamento de Instâncias EC2](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/ec2-run-instances-permissions.html)
