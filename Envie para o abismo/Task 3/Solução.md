# 📡 Identificando o Próximo Salto de Roteamento na Egress VPC

---

## 📝 Instrução

Abra a tabela de rotas **`TGW-Subnet-AZ1-EgressVPC-RT`**, associada à sub-rede **`TGWSubnet-AZ1-EgressVPC`**.  
A resposta é o **ID do recurso da AWS** definido como **destino para a rota `0.0.0.0/0`**.

---

## 🧭 Passo a Passo para Encontrar a Resposta

1. Acesse o console da Amazon VPC:  
   👉 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

2. No menu lateral, clique em **Sub-redes**.

3. Localize e marque a caixa de seleção ao lado da sub-rede:  
   ✅ **`TGWSubnet-AZ1-EgressVPC`**

4. Abaixo, clique na aba **Tabela de Rotas** para visualizar a tabela associada:  
   🔍 **`TGW-Subnet-AZ1-EgressVPC-RT`**

5. Na lista de rotas, encontre a rota com **destino `0.0.0.0/0`**.

6. Copie o valor na coluna **Destino (Target)** para esta rota.  
   - Este será o **ID do recurso AWS** (por exemplo: `igw-xxxxxxxx` ou `nat-xxxxxxxx`).

---

## ✅ Validação da Tarefa

- O valor que você copiou é o **ID do recurso do próximo salto de roteamento**.
- Insira este valor no campo de resposta da tarefa para concluir a validação.

---
