## Fundo

Para que a localização dos grupos de agentes de ameaças seja descoberta, a máquina de coordenadas precisa ser consertada. Durante o último ataque ao GDI, a parte da URL da máquina foi destruída. É fundamental que a URL de acesso à web front-end para a invocação do algoritmo seja restaurada antes que os agentes de ameaças possam atacar novamente.

## Sua tarefa

Uma função lambda chamada `bad-guy-finder` já está configurada e pronta para ser invocada. Sua tarefa é criar o "invocador" para executar essa função e retornar a string de saída necessária. Você não poderá testar a função. A única maneira de fazer com que a função produza a resposta será criar e utilizar a opção de invocação correta. Esse "invocador" deve permitir que Alice, a analista sênior da GDI, navegue até uma URL específica da web para obter a saída da função. Nenhuma alteração/adição ao código da função lambda em si é necessária para concluir esta tarefa.

Ignore todas as outras funções lambda além de `bad-guy-finder`, pois elas devem ser deixadas sozinhas para esta tarefa.

### Inventário

- **Função lambda do localizador de bandidos** - Esta é a função lambda do "algoritmo localizador de agentes de ameaças" fornecida.

### Começando

Acesse o console da AWS para verificar a função de `bad-guy-finder` e ver se algo a está invocando ou não.

### DICAS:

- As funções lambda podem ser invocadas de diversas maneiras. Para esta tarefa, há muitas maneiras de obter a string de resposta. Você precisaria configurar um gatilho de front-end.
- Um gatilho de função lambda pode ser criado diretamente da própria função lambda ou da seção de recursos de gatilho específica no console da AWS.
- Agora você deve ver um item de gatilho adicionado à janela de designer do console da função lambda. Este gatilho possui uma URL de endpoint de API que pode ser acessada para obter a string de resposta. Invoque o Lambda usando o gatilho para concluir o desafio.

### Serviços que você deve usar

- AWS Lambda
- Gateway de API da Amazon
- Balanceador de carga de aplicativo (ALB)

### Validação de Tarefas

Esta tarefa será automaticamente marcada como concluída quando:

- Você pode acessar a string de saída da função lambda por meio de um URL da web criado por você. Essa string representa as coordenadas criptografadas para a localização de um grupo de agentes de ameaças.

Além disso, você sempre pode verificar seu progresso clicando no botão Verificar meu progresso na tela Detalhes do Desafio.
