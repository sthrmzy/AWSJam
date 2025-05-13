# Plano de Fundo

O jogo para celular de carros de corrida da **Games Inc** é um dos populares jogos multijogador online. O jogador instala o jogo de corrida de carros em seus dispositivos móveis e faz o login para participar da corrida. À medida que cada jogador dirige seu carro para a corrida, o aplicativo gera dados conforme definido abaixo enquanto a corrida está em andamento.

- **player_id**: Cada jogador online é identificado usando um player_id globalmente exclusivo.
- **speed**: Velocidade do carro em determinado momento em milhas por hora.
- **distance**: Distância percorrida pelo carro desde a última sincronização de dados até agora em milhas.
- **event_time**: Data e hora em que os dados foram gerados pelo aplicativo móvel.

## Para recapitular, a arquitetura da plataforma de dados da Games Inc é mostrada abaixo.

## Gaming Inc Architecture

### Passeio pela arquitetura

- O dispositivo móvel de cada jogador registra os dados do jogo (player_id, velocidade etc.) enquanto a corrida está em andamento e os sincroniza com o **Amazon Kinesis Data Stream** a cada poucos segundos. (Usaremos esse Kinesis Data Stream como fonte de dados para todas as tarefas.)
- O **Kinesis Data Stream** está conectado ao **Amazon Managed Service para Apache Flink Studio** (Zeppelin Notebook) para processar os dados de origem e gerar uma tabela de classificação global.
- O cluster **Amazon Elasticache (Redis)** está conectado como destino para dados da tabela de classificação ao **Amazon Managed Service para Apache Flink Studio**.
- O aplicativo móvel de cada jogador chama a **API** (apoiada pela função Lambda) para recuperar a tabela de classificação e mostrá-la ao jogador.

# Tarefa

O objetivo dessa tarefa é descobrir a **fonte de dados** (**Amazon Kinesis Data Stream**) e o **destino** (**Amazon Elasticache**).

1. Encontre o nome do **Amazon Kinesis Data Stream** recebendo dados do jogo.
2. Encontre o **endpoint de configuração do cluster Amazon Elasticache** para usar como banco de dados de destino.

## Validação de Tarefas

Cole o **name da combinação host:port** de configuração de cluster do **Kinesis Data Stream** e do **endpoint de configuração de cluster do Amazon Elasticache** (separado por vírgula) na caixa de resposta na parte superior.

**Exemplo**: `my-stream,redis-host:6379`
