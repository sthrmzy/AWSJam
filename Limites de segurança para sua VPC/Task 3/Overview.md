# 🔧 Desafio: Criar e Associar Network ACLs por Camada

## 🎯 Objetivo

Segmentar o tráfego entre sub-redes dentro da **VPC chamada `Jam`** criando e associando **Network ACLs (NACLs)** específicas para cada camada da aplicação.

---

## ✅ Tarefas

### 1. Criar e associar NACL para a camada **Frontend**
- **Nome da NACL**: `FrontendACL`
- **Sub-redes a associar**:
  - `Frontend1`
  - `Frontend2`

### 2. Criar e associar NACL para a camada **Backend**
- **Nome da NACL**: `BackendACL`
- **Sub-redes a associar**:
  - `Backend1`
  - `Backend2`

### 3. Criar e associar NACL para a camada **Database**
- **Nome da NACL**: `DatabaseACL`
- **Sub-redes a associar**:
  - `DB1`
  - `DB2`

---

## 🛑 Atenção

- Você **pode criar uma NACL por sub-rede** ou **uma NACL para todas as sub-redes de uma mesma camada**. Ambas são válidas.
- **Ignore a VPC padrão** com CIDR `172.31.0.0/16`. Trabalhe **somente com a VPC chamada `Jam`**.
- **Verifique que a NACL padrão da VPC não possui nenhuma sub-rede associada** após essa configuração.

---

## 🔄 Efeito Esperado

- Após associar novas NACLs às sub-redes:
  - **A ACL padrão** da VPC `Jam` deve estar **sem nenhuma sub-rede associada**.
  - A tentativa de **acessar a página do Frontend** irá **falhar com timeout**, pois as novas NACLs vêm com **regra padrão de negação total** (não permitem tráfego algum, nem da internet).

---

## 🧪 Validação

1. Criar e associar corretamente as NACLs conforme descrito acima
2. Confirmar que a **NACL padrão** não está associada a nenhuma sub-rede
3. Atualizar a página do Frontend e verificar que ela **não carrega** (timeout)
4. Clicar em **“Check my progress”** ou aguardar validação automática

---

## ℹ️ Observação

- Network ACLs são **stateless**: você deve configurar **regras de entrada e saída separadamente** para permitir tráfego.
- Neste exercício, a falha na comunicação após associação inicial é **esperada** e serve como parte da validação.

---
