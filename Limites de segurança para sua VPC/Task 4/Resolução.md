# 🛡️ Configuração de Network ACLs (NACLs)

---

## 🌐 Front-end NACL (`acl-123abc`)

### 🔽 Regras de Entrada (Inbound)

| Nº  | Tipo        | Faixa de Portas | Fonte               | Ação   |
|-----|-------------|------------------|----------------------|--------|
| 1   | Custom TCP  | 1024-65535       | 10.0.2.0/24 (Backend1) | Allow |
| 2   | Custom TCP  | 1024-65535       | 10.0.3.0/24 (Backend2) | Allow |
| 10  | All traffic | -                | 10.0.2.0/24 (Backend1) | Deny  |
| 11  | All traffic | -                | 10.0.3.0/24 (Backend2) | Deny  |
| 12  | All traffic | -                | 10.0.4.0/24 (DB1)      | Deny  |
| 13  | All traffic | -                | 10.0.5.0/24 (DB2)      | Deny  |
| 100 | All traffic | -                | 0.0.0.0/0             | Allow |

### 🔼 Regras de Saída (Outbound)

| Nº  | Tipo        | Faixa de Portas | Destino     | Ação   |
|-----|-------------|------------------|-------------|--------|
| 100 | All traffic | -                | 0.0.0.0/0   | Allow  |

---

## 🟡 Backend NACL (`acl-123abc`)

### 🔽 Regras de Entrada (Inbound)

| Nº  | Tipo        | Faixa de Portas | Fonte               | Ação   |
|-----|-------------|------------------|----------------------|--------|
| 1   | Custom TCP  | 1024-65535       | 10.0.4.0/24 (DB1)     | Allow |
| 2   | Custom TCP  | 1024-65535       | 10.0.5.0/24 (DB2)     | Allow |
| 10  | All traffic | -                | 10.0.0.0/24 (Frontend1) | Allow |
| 11  | All traffic | -                | 10.0.1.0/24 (Frontend2) | Allow |
| 12  | All traffic | -                | 10.0.4.0/24 (DB1)     | Deny  |
| 13  | All traffic | -                | 10.0.5.0/24 (DB2)     | Deny  |

### 🔼 Regras de Saída (Outbound)

| Nº  | Tipo        | Faixa de Portas | Destino     | Ação   |
|-----|-------------|------------------|-------------|--------|
| 100 | All traffic | -                | 0.0.0.0/0   | Allow  |

---

## 🔴 Database NACL (`acl-123abc`)

### 🔽 Regras de Entrada (Inbound)

| Nº  | Tipo        | Faixa de Portas | Fonte               | Ação   |
|-----|-------------|------------------|----------------------|--------|
| 1   | All traffic | -                | 10.0.2.0/24 (Backend1) | Allow |
| 2   | All traffic | -                | 10.0.3.0/24 (Backend2) | Allow |
| 10  | All traffic | -                | 10.0.0.0/24 (Frontend1) | Deny  |
| 11  | All traffic | -                | 10.0.1.0/24 (Frontend2) | Deny  |

### 🔼 Regras de Saída (Outbound)

| Nº  | Tipo        | Faixa de Portas | Destino     | Ação   |
|-----|-------------|------------------|-------------|--------|
| 100 | All traffic | -                | 0.0.0.0/0   | Allow  |
