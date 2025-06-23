# Análise e Diagnóstico de Roteamento

## O roteamento entre as diferentes sub-redes agora se parece com o design, o que você pode confirmar por:

1. Navegue até **VPC** -> **Suas VPCs** e selecione a **VPC** listada nas propriedades de saída do desafio.
2. Selecione a aba **Mapa de recursos** para visualizar as tabelas de rotas, sub-redes e outras conexões de rede.
3. Passe o mouse sobre uma sub-rede ou tabela de rotas para ver as associações.

No entanto, ao atualizar o endpoint do balanceador de carga, você ainda não consegue acessar o site.

---

## Começando

A **arquitetura de referência** está abaixo.

*(Abrir imagem em nova aba)*

Você pergunta ao **Engenheiro Júnior** sobre os **grupos de segurança**, o que eles criaram e atribuíram a quais recursos?

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

- **Grupos de segurança EC2**
- **Instâncias EC2**
- **RDS**

---

## Sua tarefa

Atualize as configurações dos **grupos de segurança** para que o tráfego de aplicativo apropriado possa atingir todas as camadas da arquitetura.

Você suspeita que pode haver mais problemas, então não se surpreenda se o **grupo-alvo** continuar relatando que a instância não está íntegra.

---

## Validação de Tarefas

O sistema validará automaticamente se você concluiu a tarefa corretamente e o notificará. Você também pode clicar em **"Verificar meu progresso"** no topo desta página.

---

## Pistas

*(Aqui você pode adicionar pistas adicionais conforme necessário)*
