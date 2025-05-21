# 📡 Identificação do Destino da Rota 0.0.0.0/0 na Tabela vpc1-tgw-rt

---

## 📝 Instruções

Abra a tabela de rotas **`vpc1-tgw-rt`** e encontre a rota para **`0.0.0.0/0`**.  
O **destino (ID do anexo do Transit Gateway - TGW Attachment ID)** é a **resposta** que você deve fornecer.

---

## 🔧 Como Visualizar a Tabela de Rotas `vpc1-tgw-rt` no Console

1. Acesse o console da Amazon VPC:  
   👉 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

2. No painel de navegação à esquerda, clique em:  
   **Tabelas de Rotas do Gateway de Trânsito**

3. Selecione a tabela de rotas **`vpc1-tgw-rt`** para visualizar suas configurações.

4. Localize a rota com destino **`0.0.0.0/0`**.

5. Copie o valor do **"Alvo"** (Target), que será o **ID do Anexo do TGW** (ex: `tgw-attach-xxxxxxxxxxxxxxxxx`).

---

## ✅ Resultado Esperado

- O **TGW Attachment ID** associado à rota **`0.0.0.0/0`** será a **resposta** correta a ser inserida no campo de validação.

---
