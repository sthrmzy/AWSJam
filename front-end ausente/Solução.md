### Resumo rápido (o caminho mais simples)

1.  Abrir a função `bad-guy-finder` no console do Lambda.
2.  Em `Designer` → `Add trigger`, escolher `API Gateway` (`HTTP API`) e criar uma API pública (`Open`).
3.  Salvar — o console cria o endpoint e adiciona o gatilho. Copie a `API endpoint URL` e abra no navegador: a saída da função aparecerá.

### Instruções detalhadas — Console (recomendado)

1.  Faça login no Console AWS e vá para `Lambda` → `Functions`.
2.  Clique em `bad-guy-finder`.
3.  Na página da função, role até a área `Designer` (parte superior).
4.  Clique em `Add trigger` (ou no ícone `+` perto de `Designer`).
5.  Em `Trigger configuration`:
    -   **Tipo de trigger**: `API Gateway`.
    -   **API type**: escolha `HTTP API` (mais simples e moderno).
    -   **API**: `Create an API`.
    -   **Security**: `Open` (se quiser que qualquer pessoa com a URL consiga acessar — para o laboratório isso normalmente é o esperado).
    -   **Stage name**: deixe `default` ou `prod`.
6.  Clique em `Add` / `Create`. O console normalmente adiciona automaticamente a permissão necessária (`lambda:AddPermission`) para que o API Gateway invoque a Lambda.
7.  Após salvo, olhe no painel do designer — você verá o trigger `API Gateway` com um `API endpoint` (ou vá para `Configuration` → `Triggers` e lá estará).
8.  Copie a `Invoke URL` / `API endpoint` e cole no navegador. Ao acessar a URL o Lambda será chamado e você verá a string de saída (as coordenadas criptografadas).
