# Caso: Problema no Balanceador de Carga e Grupo de Destino

Você está se reunindo com o engenheiro de rede júnior para entender o progresso que ele fez.

Eles afirmam que ficaram confusos e não conseguiram acertar as configurações. As conexões com as instâncias do WordPress não estão passando pelo Balanceador de Carga.

## Hora de trabalhar!

### Começando

1. Obtenha a URL do site WordPress na guia **Propriedades de saída** (na seção de navegação à esquerda).
2. Você carrega a URL do site WordPress, mas o site não carrega.
3. Você se senta com o engenheiro júnior e começa a analisar o diagrama, confirmando todas as configurações.
![imagem](https://github.com/sthrmzy/AWSJam/blob/main/3%20n%C3%ADveis%20de%20dor!!/3TiersofPainJamChallenge.png)

Você decide que o melhor curso de ação é solucionar problemas de arquitetura em uma camada de cada vez, começando pela camada de borda e avançando.

### Investigando

1. **Verifique a integridade do grupo de destino** (EC2 -> Grupos de destino) e o **host de destino** está listado como **"Não utilizado"**.
2. Investigue mais a fundo clicando na aba **Destinos** para ver a lista de destinos registrados.
3. Os detalhes do status de integridade em **Destinos registrados** dizem que **“O grupo de destino não está configurado para receber tráfego do balanceador de carga”**.

---

## Inventário

- **VPC** que começa com **Main-VPC**
- **Sub-redes**
- **Tabelas de Rota**
- **Grupos de Segurança**
- **Balanceador de carga de aplicativo**
- **Grupo-alvo**
- **Servidor WordPress**
- **Banco de dados RDS**

---

## Serviços que você deve usar

- **Balanceadores de carga EC2**
- **Grupos-alvo do EC2**

---

## Sua tarefa

Resolva quaisquer problemas com o balanceador de carga e a configuração do grupo de destino. Você suspeita que possa haver mais problemas, então não se surpreenda se a instância continuar com problemas.

---

## Validação de Tarefas

O sistema validará automaticamente se você concluiu a tarefa corretamente e o notificará. Você também pode clicar em **"Verificar meu progresso"** no topo desta página.
