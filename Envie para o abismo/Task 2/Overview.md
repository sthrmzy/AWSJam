# 🌐 Análise de Tráfego via AWS Transit Gateway

---

## 🧩 **Fundo**

A tarefa anterior ajudou você a entender que o tráfego da **VPC-1** é enviado para o **Transit Gateway**.  
Mas como o Transit Gateway afeta esse tráfego?  
Para onde ele é enviado, ou seja, **roteado**?

---

## 🎯 **Sua Tarefa**

🔍 Revise a configuração do **Transit Gateway** e descubra como o tráfego para a **Internet** da **VPC-1** é tratado.

---

## 🚀 **Começando**

Para visualizar **tabelas de rotas do gateway de trânsito** usando o console:

1. Acesse o console da AWS VPC:  
   👉 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)

2. No painel de navegação, selecione:  
   🧭 **Tabelas de Rotas do Gateway de Trânsito**

3. Selecione uma tabela de rotas para exibir suas configurações.

---

## 📦 **Inventário**

| Recurso     | Anexo      | Tabela de Rotas     |
|-------------|------------|---------------------|
| VPC-1       | `vpc1-att` | `vpc1-tgw-rt`       |
| VPC-2       | `vpc2-att` | `vpc2-tgw-rt`       |
| Saída-VPC   | `vpc3-att` | `vpc3-tgw-rt`       |

---

## 🏗️ **Arquitetura**

📌 *Figura ilustrativa (não incluída aqui)*

---

## 🛠️ **Serviços que você deve usar**

- **AWS Transit Gateway**

---

## ✅ **Validação de Tarefas**

🔎 Encontre o **ID do componente do Gateway de Trânsito** para o qual o tráfego da internet é roteado.

📝 **Insira-o no campo de resposta.**

---
