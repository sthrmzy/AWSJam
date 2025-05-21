# Configuração de ACLs de Rede - Desafio Jam!

## 📘 Fundo

Atualmente, sua ACL de rede está "vazia", contendo apenas a regra padrão que **nega todo tráfego Inbound e Outbound**. Sua tarefa é criar regras para permitir e negar comunicação entre diferentes camadas da aplicação conforme especificado abaixo.

⚠️ **Importante:**  
As ACLs de rede **não têm estado**. Portanto, o tráfego de retorno **também precisa ser explicitamente permitido** com portas efêmeras (TCP custom: 1024-65535).

---

## ✅ Diretrizes Gerais

- **Portas Efêmeras:** Use `Custom TCP` (portas de 1024-65535)
- **Tráfego de Internet ou Camada Completa:** Use `All traffic`
- **Regras por Nível (camada):** Use o CIDR da sub-rede como origem/destino
- **Organização das Regras:** Use números em incrementos (ex.: 100, 110, 120…)  
- **Regras são avaliadas em ordem:** A avaliação para na **primeira correspondência**
- **Sempre adicione regras explícitas de negação mesmo que exista a regra padrão!**

---

## 🔐 Regras de ACL por Camada

### 🌐 Front-end

#### Entrada (Inbound)

| Nº | Tipo          | Protocolo | Porta(s)       | Origem       | Ação   |
|----|---------------|-----------|----------------|--------------|--------|
| 100 | Custom TCP    | TCP       | 1024-65535     | Backend1 CIDR | ALLOW |
| 110 | Custom TCP    | TCP       | 1024-65535     | Backend2 CIDR | ALLOW |
| 120 | All traffic   | ALL       | ALL            | Backend1 CIDR | DENY  |
| 130 | All traffic   | ALL       | ALL            | Backend2 CIDR | DENY  |
| 140 | All traffic   | ALL       | ALL            | DB1 CIDR      | DENY  |
| 150 | All traffic   | ALL       | ALL            | DB2 CIDR      | DENY  |
| 160 | All traffic   | ALL       | ALL            | 0.0.0.0/0     | ALLOW |

#### Saída (Outbound)

| Nº | Tipo        | Protocolo | Porta(s) | Destino     | Ação  |
|----|-------------|-----------|----------|-------------|-------|
| 100 | All traffic | ALL       | ALL      | 0.0.0.0/0   | ALLOW |

---

### ⚙️ Backend

#### Entrada (Inbound)

| Nº | Tipo          | Protocolo | Porta(s)       | Origem        | Ação   |
|----|---------------|-----------|----------------|---------------|--------|
| 100 | Custom TCP    | TCP       | 1024-65535     | DB1 CIDR       | ALLOW |
| 110 | Custom TCP    | TCP       | 1024-65535     | DB2 CIDR       | ALLOW |
| 120 | Custom TCP    | TCP       | 1024-65535     | Frontend1 CIDR | ALLOW |
| 130 | Custom TCP    | TCP       | 1024-65535     | Frontend2 CIDR | ALLOW |
| 140 | All traffic   | ALL       | ALL            | DB1 CIDR       | DENY  |
| 150 | All traffic   | ALL       | ALL            | DB2 CIDR       | DENY  |

#### Saída (Outbound)

| Nº | Tipo        | Protocolo | Porta(s) | Destino   | Ação  |
|----|-------------|-----------|----------|-----------|-------|
| 100 | All traffic | ALL       | ALL      | 0.0.0.0/0 | ALLOW |

---

### 🗄 Banco de Dados

#### Entrada (Inbound)

| Nº | Tipo          | Protocolo | Porta(s)       | Origem        | Ação   |
|----|---------------|-----------|----------------|---------------|--------|
| 100 | Custom TCP    | TCP       | 1024-65535     | Backend1 CIDR | ALLOW |
| 110 | Custom TCP    | TCP       | 1024-65535     | Backend2 CIDR | ALLOW |
| 120 | All traffic   | ALL       | ALL            | Frontend1 CIDR | DENY |
| 130 | All traffic   | ALL       | ALL            | Frontend2 CIDR | DENY |

#### Saída (Outbound)

| Nº | Tipo        | Protocolo | Porta(s) | Destino   | Ação  |
|----|-------------|-----------|----------|-----------|-------|
| 100 | All traffic | ALL       | ALL      | 0.0.0.0/0 | ALLOW |

---

## 🧪 Validação

- Verifique se cada camada (Front-end, Backend, Banco de Dados) está se comunicando apenas com os destinos permitidos.
- Teste o tráfego de entrada e saída usando ferramentas como `ping`, `telnet`, `curl` ou `nc`.
- Use a página da aplicação para testar o fluxo entre camadas conforme esperado.

---

## 📌 Observações Finais

- Ignore a **VPC padrão** (CIDR `172.31.0.0/16`)
- Sempre use a **VPC chamada "Jam!"**
- Não modifique regras de NACL: remova e adicione novamente caso necessário
- Regra padrão `DENY` não conta como regra explícita – adicione você mesmo!

