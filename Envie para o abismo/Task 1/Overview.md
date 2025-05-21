# Desafio: Rastrear Tráfego EC2 para a Internet via Redes Multi-VPC

## Fundo

Desanimado pela falta de um **diagrama de arquitetura adequado**, você decide descobrir por conta própria e rastrear o **tráfego do servidor EC2 na VPC-1** até a Internet.

Você se lembra de uma conversa com a equipe do **DocSkimmaz** sobre a *configuração de saída de Internet centralizada*, que **permite que servidores EC2 em diferentes VPCs usem um único IP elástico como origem durante conexões com a Internet**.

---

## Sua Tarefa

Para rastrear o tráfego, responda à seguinte pergunta:

> **Se o servidor EC2 na VPC-1 quiser se comunicar com a Internet (ou seja, qualquer rede diferente de sua própria sub-rede `10.0.0.0/28` ou VPC `10.0.0.0/24`), para onde ele vai — ou melhor, para onde é roteado (primeiro)?**

---

## Começando

Você pode **determinar a qual tabela de rotas uma sub-rede está associada** observando os detalhes da sub-rede no console do Amazon VPC:

### Passos:

1. Acesse o console do Amazon VPC:  
   👉 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

2. No painel de navegação, selecione **Sub-redes**.

3. Selecione a aba **Tabela de Rotas** para visualizar o **ID da tabela de rotas** e suas **rotas associadas**.

---

## Observação Importante

⚠️ Durante testes de **acesso de saída à Internet** em instâncias do EC2 no **VPC1 ou VPC2**, apenas os **IPs públicos `1.1.1.1` e `8.8.8.8`** são permitidos para tráfego de saída.

---

## Inventário de Sub-redes

| Nome                            | CIDR              |
|---------------------------------|-------------------|
| Sub-rede privada-VPC1-AZ1       | `10.0.0.0/28`     |
| TGWSubnet-VPC1-AZ1              | `10.0.0.16/28`    |
| Sub-rede privada-VPC1-AZ2       | `10.0.0.128/28`   |
| TGWSubnet-VPC1-AZ2              | `10.0.0.144/28`   |
| Sub-rede privada-VPC2-AZ1       | `10.0.1.0/28`     |
| TGWSubnet-VPC2-AZ1              | `10.0.1.16/28`    |
| Sub-rede privada-VPC2-AZ2       | `10.0.1.128/28`   |
| TGWSubnet-VPC2-AZ2              | `10.0.1.144/28`   |
| PublicSubnet-AZ1-EgressVPC      | `100.64.0.0/28`   |
| TGWSubnet-AZ1-EgressVPC         | `100.64.0.16/28`  |
| PublicSubnet-AZ2-EgressVPC      | `100.64.0.128/28` |
| TGWSubnet-AZ2-EgressVPC         | `100.64.0.144/28` |

---

## Arquitetura

📌 *Um diagrama de arquitetura é mencionado, mas não fornecido. Certifique-se de entender os relacionamentos entre as VPCs, sub-redes privadas, sub-redes do Transit Gateway (TGW) e sub-redes públicas.*

---

## Serviços AWS Utilizados

- **Amazon VPC**
- **AWS Transit Gateway**
- **NAT Gateway**
- **EC2**
- **Route Tables**

---

## Validação da Tarefa

✅ **Insira o ID do recurso do salto de roteamento (next hop)** no campo de resposta, que representa o **primeiro destino para onde o tráfego é roteado** a partir do EC2 na VPC-1 em direção à Internet.

---

> 💡 Dica: Verifique a rota padrão (`0.0.0.0/0`) na tabela de rotas da sub-rede onde o EC2 está implantado para encontrar o "next hop", que normalmente será um **Transit Gateway (tgw-xxxxxxxx)**.
