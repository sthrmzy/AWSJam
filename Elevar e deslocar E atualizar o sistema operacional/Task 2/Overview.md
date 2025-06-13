## Fundo
Sua primeira tarefa é verificar se o servidor local está pronto para migrar para a AWS.

Um dos seus colegas instalou o agente do AWS Application Migration Service em um servidor Windows e iniciou a replicação para a AWS.

## Sua tarefa
No AWS Application Migration Service, configure as configurações de pós-lançamento para executar a automação de atualização do Windows.  
A ação precisa estar no estado **Ativo**.

## Começando
Use o AWS Console para acessar o AWS Application Migration Service.

## Inventário
- Um servidor já estará configurado no AWS Application Migration Service  
- Um perfil de instância do IAM `UpgradeInstanceProfile` para usar como um parâmetro de runbook  
- Uma atualização de sub-rede `Subnet` para usar como um parâmetro de runbook  
- Uma função IAM `UpgradeAutomationRole` para usar como um parâmetro de runbook

## Serviços que você deve usar
- Serviço de Migração de Aplicativos da AWS

## Validação de Tarefas
Esta tarefa será concluída automaticamente alguns minutos após a ativação da ação Pós-lançamento.  
Opcionalmente, você pode acionar a verificação manualmente clicando no botão **"Verificar meu progresso"**.
