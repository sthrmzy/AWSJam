![Overview](https://github.com/sthrmzy/AWSJam/blob/main/Limites%20de%20seguran%C3%A7a%20para%20sua%20VPC/Task%202/Task2.png)

# Desafio: Migrar de uma VPC Plana para uma VPC Segmentada Usando Grupos de Segurança

## 🎯 Objetivo

Segmentar as cargas de trabalho dentro da VPC **Jam** utilizando **Grupos de Segurança (Security Groups)**.

## 🛡️ Conceitos Importantes

- Um **Grupo de Segurança (SG)** atua como um **firewall virtual** no nível da instância.
- Cada instância pode ter até **5 grupos de segurança**.
- Grupos de segurança são **stateful**:
  - Requisições de saída autorizadas permitem **respostas automáticas**, sem necessidade de regra de entrada correspondente.
  - E vice-versa.
- Você pode definir **regras de entrada e saída** com base em:
  - Blocos **CIDR IPv4**
  - **Outros grupos de segurança** (recomendado)

## ⚙️ Situação Atual

- **Todas as instâncias têm um SG associado**.
- **SG-Frontend** permite tráfego da internet (`0.0.0.0/0`).
- **SG-Backend** permite tráfego de **todo o CIDR da VPC**.
- **SG-Database** permite tráfego de **todo o CIDR da VPC**.

## 🧪 Tarefa

**Alterar as regras dos grupos de segurança para:**

1. Permitir **tráfego da internet → Frontend** (via CIDR)
2. Permitir **tráfego do Frontend → Backend** (via grupo de segurança)
3. Permitir **tráfego do Backend → Banco de Dados** (via grupo de segurança)

> ⚠️ **Atenção:** Não use o CIDR da VPC para permitir tráfego entre camadas. Use **referências de SG**.

---

## ✅ Configuração Correta dos Grupos de Segurança

### SG-Frontend
- **Entrada**:
  - Tipo: HTTP
  - Porta: 80
  - Origem: `0.0.0.0/0` (internet)
- **Remover** regras que permitem acesso de Backend ou DB

### SG-Backend
- **Entrada**:
  - Tipo: HTTP
  - Porta: 80
  - Origem: **SG-Frontend**
- **Remover** regra com origem CIDR da VPC

### SG-Database
- **Entrada**:
  - Tipo: HTTP
  - Porta: 80
  - Origem: **SG-Backend**
- **Remover** regra com origem CIDR da VPC

---

## 🧭 Validação da Tarefa

1. Alterar os SGs conforme descrito acima
2. Atualizar a página web do desafio
3. Verificar que:
   - A camada **Frontend aceita apenas da Internet**
   - A camada **Backend aceita apenas do Frontend**
   - A camada **Database aceita apenas do Backend**
4. Clique em **"Check my progress"** ou aguarde validação automática

---

## 📌 Observações Finais

- Grupos de segurança **não negam tráfego**, apenas **permitem**.
- Mesmo que a camada de frontend **aceite tráfego da internet**, não há como impedir totalmente o backend ou database de iniciar conexões com ela.
- Certifique-se de que **todas as instâncias estão com os SGs corretos** aplicados.
- **Ignore a VPC padrão** (`172.31.0.0/16`) — o desafio se refere **apenas à VPC chamada `Jam`**.

---
