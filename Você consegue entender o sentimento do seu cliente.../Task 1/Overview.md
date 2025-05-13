## Plano de fundo

A equipe de análise precisa consolidar as avaliações dos clientes e realizar análises de sentimentos. Como você foi encarregado de obter os insights de sentimento das avaliações do produto você precisa executar um trabalho de análise do Amazon Comprehend que cria uma saída arquivo com os dados da análise.

## Sua tarefa

Um arquivo de texto contendo avaliações de clientes sobre um produto está disponível no nome do bucket do S3 prefixado com `s3productreview`. Use isso como um arquivo de entrada para criar o arquivo de saída com detalhes do sentimento para cada avaliação do produto usando o trabalho de análise do Amazon Comprehend. O arquivo de saída deve ser criado no mesmo bucket do S3. Depois que o arquivo de saída é criado, a tarefa é completo.

## Inventário

Sua conta da AWS é provisionada com o seguinte:

- Bucket S3 prefixado com: `s3productreview`
- Arquivo de avaliação do produto dentro do bucket do S3
- Função do IAM `S3AccessRoleComprehend`
- Permissões mínimas necessárias para você concluir esta tarefa

## Começando

Navegue até o console do S3 e identifique o bucket e o arquivo necessários para essa tarefa. Copie o URI S3 do arquivo e siga em frente ao Amazon Comprehend Console para criar um trabalho de análise de sentimentos com o identificou o arquivo S3 como entrada.

Para dados de saída, especifique o mesmo valor de bucket do S3 sem nenhum nome de objeto.

## Serviços envolvidos

- Amazon S3  
- Amazon Comprehend

## Validação de tarefas

Quando o trabalho de análise do Amazon Comprehend for concluído com êxito, insira o nome do trabalho de análise no campo localizado no no topo desta página que diz **Enter answer here** e clique em **enviar** para obter o crédito.
