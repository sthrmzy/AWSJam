# 🔧 Etapas para Roteamento de Solicitações de Registro de Dispositivo Único

Este guia passo a passo ajudará você a configurar corretamente a regra do **Amazon EventBridge** para rotear eventos de registro de dispositivo único.

---

## ✅ Passo 1: Editar a Regra de Evento

1. Acesse o **Console de Gerenciamento da AWS**.
2. Certifique-se de estar na **região correta** onde o desafio está implantado.
3. Navegue até **Amazon EventBridge > Barramentos de eventos**.
4. Selecione o **barramento de eventos personalizado**:  
   `register-device-event-bus`.
5. Vá para a aba **Regras**.
6. Selecione a regra **eb-single-device-rule**.
7. Clique em **Editar**.
8. Na seção **Padrão de Evento**, cole o seguinte código:

    ```json
    {
      "detail": {
        "registration-type": [
          {
            "prefix": {
              "equals-ignore-case": "single"
            }
          }
        ]
      }
    }
    ```

9. Clique em **Avançar**.
10. Selecione **Pular para revisão e atualização**.
11. Clique em **Atualizar Regra**.

---

## ✅ Passo 2: Enviar Evento de Teste

1. Ainda no Console da AWS, permaneça na **mesma região**.
2. Acesse **Amazon EventBridge > Barramentos de eventos**.
3. Na lista de barramentos personalizados, selecione o botão de opção ao lado de  
   `register-device-event-bus`.
4. Clique no link **Enviar eventos**.
5. Preencha os campos:
   - **Origem do evento**: `task.singledevice.com`
   - **Tipo de detalhe**: `single-device`
6. Na seção **Detalhes do Evento**, insira o seguinte JSON:

    ```json
    {
      "registration-type": "single-device",
      "device-count": 1
    }
    ```

7. Clique em **Enviar**.

---

## 🎉 Conclusão

- A tarefa será **concluída automaticamente** se tudo estiver configurado corretamente.
- Você pode clicar em **"Verificar meu progresso"** para confirmar a conclusão.

---

## 🙌 Obrigado!

Obrigado por aceitar este desafio!  
Esperamos que você tenha tido uma ótima **experiência de aprendizado** com o Amazon EventBridge.
