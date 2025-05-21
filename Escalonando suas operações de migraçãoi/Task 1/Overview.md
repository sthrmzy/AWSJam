# Por que o PowerShell chegou ao Linux?

## Cenário

Seu colega implantou um Documento de Comando do Systems Manager para reconfigurar o Proxy em instâncias migradas da AWS.  
Antes da migração, o administrador costumava efetuar login em cada host, um por um, mas agora os documentos de automação devem fazer a maior parte do trabalho pesado.

O documento deve ser compatível com Windows e Linux, e você sabe que ele foi testado com sucesso em instâncias do Windows.  
No entanto, desde que a migração das instâncias do Linux foi iniciada, o documento SSM começou a apresentar falhas com o seguinte erro:

failed to run commands: fork/exec /usr/bin/pwsh: no such file or directory


Observando o erro, você descobre que o SSM está tentando executar o script do PowerShell para instâncias do Windows nas instâncias do Linux.  
Isso nunca vai funcionar.

---

## Inventário

- Documento: **ConfigureProxy**

---

## Serviços que você deve usar

- **Gerente de sistemas da AWS**

---

## Sua tarefa

Sua primeira tarefa é analisar o documento de comando chamado `ConfigureProxy`  
e descobrir como executar cada etapa somente para o sistema operacional correto.

---

## Validação de Tarefas

O sistema validará automaticamente se você concluiu a tarefa corretamente e o notificará.  
Você também pode clicar em **"Verificar meu progresso"** no topo desta página.
