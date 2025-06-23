# Caso: Problema nas Conexões com as Instâncias do WordPress

Você está se reunindo com o engenheiro de rede júnior para entender o progresso que ele fez.

Eles afirmam que ficaram confusos e não conseguiram acertar as configurações. As conexões com as instâncias do WordPress não estão passando pelo Balanceador de Carga.

---

## Começando

1. Observando o **EC2 -> Balanceadores de carga -> Mapa de recursos**, agora há um caminho do balanceador de carga para o grupo de destino para o tráfego da web.
2. Obtenha a **URL do site WordPress** na guia **Propriedades de saída** (na seção de navegação à esquerda).
3. Você carrega a URL do site WordPress, mas o site não carrega.
  ![imagem](https://github.com/sthrmzy/AWSJam/blob/main/3%20n%C3%ADveis%20de%20dor!!/3TiersofPainJamChallenge.png)
   

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

- **Tabelas de rotas VPC**
- **Sub-redes VPC**

---

## Verificação: Roteamento da Camada do Aplicativo

Verifique se a **camada do aplicativo** está roteando corretamente.

**Dica:** Adicionar rotas às **tabelas de rotas** não é obrigatório (nem permitido) para resolver esta tarefa. Sinta-se à vontade para revisar as tabelas de rotas para entender o que elas fazem, mas você não é obrigado a alterar essas rotas.

---

## Sua tarefa

Resolva quaisquer problemas com o balanceador de carga e a configuração do grupo de destino. Você suspeita que possa haver mais problemas, então não se surpreenda se o **grupo-alvo** continuar relatando que a instância não está íntegra.

---

## Validação de Tarefas

Confira **meu progresso** no topo desta página.
