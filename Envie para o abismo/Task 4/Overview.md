# 🔒 Bloqueando Tráfego Entre VPC-1 e VPC-2 Usando o AWS Transit Gateway

---

## 🧠 **Fundo**

Você inferiu corretamente que o **Internet Gateway** é o destino final do tráfego após sair do **NAT Gateway** e conseguiu rastrear o caminho da solicitação com sucesso!

Agora, um novo desafio:  
Você recebeu um e-mail da equipe **DocSkimmaz** pedindo para bloquear o tráfego entre **VPC-1** e **VPC-2**, mesmo para futuras instâncias e sub-redes.

---

## 📧 **E-mail Recebido**

**Dia:** Penúltimo  
**Assinatura:** Por favor, conserte, obrigado.

> Caro engenheiro da AWS,  
>
> Anexando um diagrama de fluxo de tráfego explicando a configuração da Saída Centralizada. Como mencionado anteriormente, tentamos Grupos de Segurança e parece que não funciona.  
> Você pode verificar, mas recomendamos que **não faça nenhuma alteração**. Ah! E já mencionamos que **não gostamos de NACLs**?  
>
> Observação: configuramos o acesso do Gerenciador de Sessões a ambas as instâncias do EC2 para que você possa testar a conectividade entre as VPCs após qualquer alteração feita.  
>
> Espero que você conserte isso logo!  
>
> Obrigado,  
> Líder de Equipe, DocSkimmaz  
> *Enviado da minha mesa de trabalho*

---

## 🧪 **Começando**

### ✔️ Etapas para Verificar o Problema

1. Acesse o console EC2:  
   👉 [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/)

2. No painel de navegação, selecione **Instâncias**.

3. Selecione a instância da **VPC-1**, clique em **Conectar** e use o **Gerenciador de Sessões**.

4. Execute:  
   ```bash
   ping 10.0.1.10
