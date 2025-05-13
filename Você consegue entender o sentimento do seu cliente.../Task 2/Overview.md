## Plano de fundo  
Parabéns por criar com sucesso o trabalho de análise de sentimentos. A equipe está feliz porque estamos um passo mais perto de obter os resultados. O trabalho do Amazon Comprehend agora está concluído e a saída está disponível no mesmo bucket do S3. Os dados analisados precisam ser carregados em uma tabela do Amazon Reshift para ajudar a gerência da empresa a realizar análises e relatórios históricos. Antes de carregar os dados de saída no Redshift Cluster, as permissões necessárias para que o cluster acesse os dados no bucket do S3 precisam estar estabelecidas.

## Sua tarefa  
Associe a função IAM criada que permitirá o Redshift cluster para acessar objetos do S3. Ignore os erros no console do Amazon Redshift.

## Inventário  
Sua conta da AWS é provisionada com o seguinte:
- Bucket S3 prefixado com: s3productreview
- Cluster Redshift
- Função IAM S3AccessRoleRedshift
- Permissões mínimas necessárias para você concluir esta tarefa  
Verifique a guia output properties à esquerda para ver os detalhes do identificador do cluster Redshift.

## Começando  
Navegue até o console do IAM e crie uma função do IAM para o Redshift Service com os privilégios necessários para acessar seu bucket do S3.

## Serviços envolvidos  
Amazon Redshift  
ERA O OBJETIVO  

## Validação de tarefas  
Depois que a função do IAM for associada ao cluster do Redshift, a tarefa será automaticamente validada para conclusão. Como alternativa, você pode clicar em Check my Progress para verificar o status.
