# 🔧 Passo a Passo para Configurar os Grupos de Segurança

## 1. Grupo de Segurança do **Frontend** (`SG-Frontend`)

**Permitir**: Acesso da **Internet** na porta **80 (HTTP)**

### ➕ Regras de Entrada:
- **Tipo**: HTTP  
- **Porta**: 80  
- **Origem**: `0.0.0.0/0` (Internet)

### 🚫 Ações adicionais:
- **Remover** qualquer regra de entrada que permita tráfego de **Backend** ou **Database**

### ➖ Regras de Saída:
- **Manter padrão** (geralmente permite todo o tráfego de saída)

---

## 2. Grupo de Segurança do **Backend** (`SG-Backend`)

**Permitir**: Acesso **apenas da camada Frontend**

### ➕ Regras de Entrada:
- **Tipo**: HTTP  
- **Porta**: 80  
- **Origem**: **SG-Frontend** (utilize o ID do grupo de segurança do Frontend)

### 🚫 Ações adicionais:
- **Remover** qualquer regra com **origem CIDR da VPC** (ex: `10.0.0.0/16`)

---

## 3. Grupo de Segurança do **Banco de Dados** (`SG-DB`)

**Permitir**: Acesso **apenas da camada Backend**

### ➕ Regras de Entrada:
- **Tipo**: HTTP  
- **Porta**: 80  
- **Origem**: **SG-Backend** (utilize o ID do grupo de segurança do Backend)

### 🚫 Ações adicionais:
- **Remover** qualquer regra com **origem CIDR da VPC** (ex: `10.0.0.0/16`)

---

## ❌ O Que **Não Fazer**

- **Não usar** o CIDR da VPC como origem nas regras internas  
  Exemplo: `10.0.0.0/16`, `172.31.0.0/16`

- **Não permitir** que o grupo de segurança do **Frontend** aceite tráfego de instâncias do **Backend** ou **Database**

---
