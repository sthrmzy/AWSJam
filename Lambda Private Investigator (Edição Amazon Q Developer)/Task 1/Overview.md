Plano de fundo  
Jason participou recentemente de uma conferência de tecnologia e viu muitos usos incríveis do AWS Lambda. Então, ele decidiu experimentar usando o AWS Lambda e o Amazon API Gateway para criar sua API RESTful.

Ele seguiu vários exemplos que conseguiu encontrar, mas não consegue fazer com que a RestAPI do Amazon API Gateway exiba a resposta de sua função do AWS Lambda.

Para tornar sua experiência de codificação muito mais fácil e rápida, ele recorre ao Amazon Q Developer para gerar o código para ele.

Sua tarefa  
Corrija o código Python do Lambda para obter a resposta secreta do conteúdo depois de ligar para ApiGatewayInvokeURL.

Começando  
No Output Properties (menu à esquerda), clicar em ApiGatewayInvokeURL exibe {"message": "Internal server error"}. Você precisará corrigir esse erro.  
Comece dando uma olhada no grupo Amazon CloudWatch Log API-Gateway-Execution-Logs_[ApiGatewayId]/prod (confira Output Properties para descobrir o valor real de ApiGatewayId). Para fazer isso, clique no botão AWS Console (canto superior direito da página) para iniciar o AWS Management Console e, em seguida, navegue até o console do Amazon CloudWatch.  
Examine os registros para ver o que pode estar causando o Internal server error. Dica: Somente a função Python do Lambda precisa ser corrigida para resolver esse desafio. Não há necessidade de modificar outros recursos, como variáveis de ambiente do Lambda, buckets e objetos do S3, etc.  
Para usar o Amazon Q Developer no console do AWS Lambda:

- Navegue até o console do AWS Lambda e abra a função do Lambda chamada lambda-pi.  
- Verifique se o AWS Q Developer está habilitado clicando em Amazon Q no canto inferior esquerdo da janela de código. O status deve ser exibido como Currently RUNNING.  
- O Amazon Q gera o código python no console do AWS Lambda e pode ajudar a retornar o conteúdo em cabeçalhos de texto simples. Para ver as sugestões de código geradas, você pode começar a digitar comentários ou pressionar Option + C (no macOS) ou Alt + C (no Windows). Consulte Ações do usuário para obter mais opções de atalhos de teclado.  
- Não se esqueça de salvar e implantar o código atualizado.

Alguns recursos úteis:

- Preenchimento de código de linha única  
- Configurar integrações de proxy Lambda no API Gateway  

Inventário  
Do Output Properties (menu à esquerda):

- URL de invocação do Amazon API Gateway RestAPI (ApiGatewayInvokeURL) — Função AWS Lambda (LambdaFunctionName)  
- ID do API Gateway (ApiGatewayId) para lambda-pi  

Serviços que você deve usar  
- Amazon API Gateway RestAPI  
- Função AWS Lambda  
- Grupos de log do Amazon CloudWatch (o Log Insights e o Live Tail não são necessários)  
- Desenvolvedor Amazon Q  

Validação de tarefas  
Para concluir com êxito essa tarefa (e desafio), abrir o URL HTTPS (valor ApiGatewayInvokeURL) em um navegador deve exibir o conteúdo das descobertas de Tom em suas investigações. Jason precisa saber disso!

A tarefa será validada automaticamente após a conclusão, sem qualquer entrada do usuário.
