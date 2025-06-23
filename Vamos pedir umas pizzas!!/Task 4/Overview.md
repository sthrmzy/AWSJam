# Background

Você agora completou todas as configurações necessárias para as camadas **DMZ**, **Aplicação** e **DB** dessa arquitetura 3 camadas, corrigindo o ouvinte, as associações das tabelas de rotas e os grupos de segurança.

**O site ainda não está resolvendo!!!**

O problema restante deve estar nos **hosts WordPress** (instâncias EC2).

---

# Getting Started

Você e o Engenheiro Júnior examinam o **EC2 -> Launch Template** para os hosts EC2. Selecione o template e navegue até a aba **Advanced details** e role para baixo para ver os **User data**.

Você nota que os dados de usuário irão baixar e instalar o software WordPress e suas dependências da internet.

As instâncias EC2 foram criadas com roteamento incorreto. Até o momento em que você corrigiu todos os problemas de configuração, as instâncias EC2 não conseguiam alcançar a internet. Portanto, elas não possuem o software WordPress.

Você precisa reiniciar a atualização do sistema operacional e o download do software WordPress. Você pode testar essa teoria enquanto segue para o primeiro passo desta tarefa.

---

# Inventário

- **VPC** que começa com **Main-VPC**
- **Sub-redes**
- **Tabelas de Rota**
- **Grupos de Segurança**
- **Balanceador de carga de aplicativo**
- **Grupo-alvo**
- **Servidor WordPress**
- **Banco de dados RDS**

---

# Serviços que você deve usar

- **EC2 Launch Templates**
- **EC2 Instances**
- **EC2 Auto Scaling Groups**

---

# Suas Tarefas

1. Resolva o problema do **host EC2** **Unhealthy** original primeiro.
2. A aplicação deve ser altamente disponível, com um mínimo de **2 hosts** em **zonas de disponibilidade** diferentes o tempo todo.
3. Certifique-se de que os hosts em **AZ1** e **AZ2** estão **Healthy** tanto no **Auto Scaling Group** quanto no **Target Group**.

---

# Dica

- **Você não tem permissões de login**, nem precisa de acesso para fazer login nas instâncias EC2 para resolver este problema.

---

# Observação

Você precisará aguardar alguns minutos para que os novos hosts atinjam o estado **Healthy**. Agora pode ser um bom momento para revisar seu próximo desafio no Jam.

---

# Validação da Tarefa

O sistema validará automaticamente se você concluiu a tarefa corretamente e o notificará. Você também pode clicar em **"Verificar meu progresso"** no topo desta página.
