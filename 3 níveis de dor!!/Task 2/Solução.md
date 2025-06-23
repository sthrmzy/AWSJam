# Análise da Situação Atual

## Progresso
O **Application Load Balancer (ALB)** agora tem um caminho para o **Grupo de Destino (Target Group)**. Isso significa que o **"Ouvinte" (Listener)** está configurado corretamente e o ALB está tentando enviar tráfego (incluindo as verificações de saúde) para as instâncias.

## Problema
O site ainda não carrega e as instâncias provavelmente continuam sendo reportadas como **"não íntegras" (unhealthy)** no **Target Group**.

## Pista Crucial
A tarefa nos diz que **não é necessário (nem permitido) alterar as rotas nas Tabelas de Rota**. Isso é uma dica muito forte. Significa que as tabelas de rota (**Public-RTB, AppAZ1PrivRTB, AppAZ2PrivRTB**, etc.) já estão configuradas com as rotas corretas.

Se as tabelas de rota estão corretas, mas o roteamento da camada de aplicação ainda está com problemas, a causa mais provável é que as **sub-redes da aplicação** não estão associadas à tabela de rota correta.

---

# Passo a Passo para a Solução da Camada de Aplicação

## Passo 1: Corrigir a Associação da Tabela de Rota da Sub-rede da Aplicação

### Problema Identificado
As instâncias WordPress estão em sub-redes que deveriam ser **privadas** (**APP AZ1 Subnet**, **APP AZ2 Subnet**). Uma sub-rede privada, por definição, não deve ter uma rota direta para a Internet. Seu tráfego de saída para a internet deve passar por um **NAT Gateway**.

É muito provável que essas sub-redes de aplicação estejam **incorretamente associadas à tabela de rota pública (Public-RTB)**, em vez de suas respectivas tabelas de rota privadas (**AppAZ1PrivRTB** e **AppAZ2PrivRTB**).

### Justificativa da Solução

- **Funcionalidade**: A arquitetura foi projetada para que as instâncias privadas usem o **NAT Gateway** para acessar a internet (para atualizações, etc.). Se a sub-rede delas aponta para o **Internet Gateway (IGW)** através da tabela de rota pública, esse caminho é quebrado.
  
- **Segurança**: Associar uma sub-rede que contém recursos privados a uma tabela de rota pública é uma falha de segurança e configuração de rede.

- **Verificações de Saúde do ALB**: O ALB (que está em sub-redes públicas) envia verificações de saúde para os **IPs privados** das instâncias. Se a sub-rede da instância tem uma rota de volta para a internet através do IGW, isso pode criar um **roteamento assimétrico** e fazer com que as verificações de saúde falhem.

### Como Resolver

1. Acesse o **Console da AWS** e navegue até o serviço **VPC**.
2. No menu à esquerda, clique em **Sub-redes** (Subnets).
3. Localize as sub-redes onde as instâncias WordPress estão localizadas. Elas provavelmente terão nomes como **...AppAZ1Subnet...** e **...AppAZ2Subnet...**.
4. Selecione a primeira sub-rede de aplicação (ex: **...AppAZ1Subnet...**).
5. No painel de detalhes na parte inferior, clique na aba **Tabela de Rota** (Route Table).
6. Verifique a **"Tabela de Rota Atual"**. É muito provável que ela esteja associada à tabela de rota pública (**...Public-RTB...**). Este é o erro.
7. Clique no botão **Editar associação da tabela de rota** (Edit route table association).
8. Na lista suspensa **ID da Tabela de Rota** (Route Table ID), selecione a tabela de rota privada correta para essa Zona de Disponibilidade. O nome deve ser algo como **...AppAZ1PrivRTB...**. Essa é a tabela que tem a rota **0.0.0.0/0** apontando para o **NAT Gateway**.
9. Clique em **Salvar** (Save).
10. Repita os passos 4 a 9 para a segunda sub-rede de aplicação (**...AppAZ2Subnet...**), garantindo que ela seja associada à sua respectiva tabela de rota privada (**...AppAZ2PrivRTB...**).

---

## Passo 2: Validar o Resultado
