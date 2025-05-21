# 🛑 Solução para Bloquear Tráfego Entre VPC-1 e VPC-2 via NAT Gateway

---

## 🧠 Explicação

O problema ocorre porque o tráfego da **VPC-1 para a VPC-2** utiliza a rota **`0.0.0.0/0`** na tabela de rotas do Transit Gateway (**TGW**), o que envia esse tráfego para o **NAT Gateway (NAT-GW)**.  
Apesar dessa rota ser destinada ao tráfego de Internet, ela também cobre **qualquer** destino — inclusive outras VPCs internas.

### 📌 Comportamento atual:

- O **NAT-GW** traduz o IP de origem da instância na **VPC-1** antes de encaminhar para a instância da **VPC-2**.
- A **VPC-2** vê o tráfego vindo do IP **privado do NAT-GW**.
- A resposta segue para o NAT-GW, que a reencaminha para a instância original na VPC-1.
- Isso **contorna os Grupos de Segurança**, pois o tráfego é permitido na entrada/saída via **Egress VPC**.

---

## 🎯 Objetivo

Evitar que a **VPC-1 se comunique com a VPC-2** e vice-versa — inclusive para **futuras sub-redes ou instâncias** — utilizando rotas mais específicas (CIDRs das VPCs) com destino **Blackhole**.

---

## 🛠️ Solução (Passo a Passo)

### 🔹 Parte 1: Bloquear Tráfego da VPC-1 para a VPC-2

1. Acesse o Console do Amazon VPC:  
   👉 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

2. No painel de navegação, clique em **Tabelas de rotas do gateway de trânsito**.

3. Selecione a tabela de rotas: **`vpc1-tgw-rt`**.

4. Clique em **Ações** > **Criar rota estática**.

5. Em **Bloco CIDR**, insira:  

10.0.1.0/24

6. Para o **Destino**, selecione:  

Blackhole

7. Clique em **Criar rota estática**.

---

### 🔹 Parte 2: Bloquear Tráfego da VPC-2 para a VPC-1

1. Ainda no Console do Amazon VPC, vá novamente em **Tabelas de rotas do gateway de trânsito**.

2. Selecione a tabela de rotas: **`vpc2-tgw-rt`**.

3. Clique em **Ações** > **Criar rota estática**.

4. Em **Bloco CIDR**, insira:  

10.0.0.0/24

5. Para o **Destino**, selecione:  

Blackhole


6. Clique em **Criar rota estática**.



