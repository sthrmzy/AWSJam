Fundo  
Agora que você concluiu o roteamento de solicitações de dispositivos individuais, precisa rotear as solicitações de dispositivos em massa. A solicitação conterá as estruturas JSON abaixo. Você pode usar esses scripts JSON após formular a regra para verificar o resultado.

{
   "registration-type": "bulk-device",
   "device-count": 99,
   "region": "us-east-1"
  }

E

{
   "registration-type": "bulk-device",
   "device-count": 100,
   "region": "eu-west-1"
}

Inventário  
Para facilitar esta tarefa, o seguinte foi configurado neste ambiente.  
Ônibus de eventos com nome `register-device-event-bus`  
Regra de evento com nome `eb-register-bulk-device-rule`  
Função lambda com nome `register-bulk-devices-function` como alvo  

Sua tarefa  
Agora você precisa usar a sintaxe de filtragem apropriada do EventBridge e formulá-la com base na regra mencionada acima. A regra deve identificar as solicitações conforme o requisito abaixo e encaminhá-las para `register-bulk-devices-function`

Exigência  
Todas as solicitações que têm `registration-type` valor começando com `bulk` **AND**  
O `device-count` valor entre 1 e 99 para qualquer região **OU** as solicitações que têm valor de região `eu-west-1` (ou seja, no caso de `eu-west-1`, o valor de contagem de dispositivos pode exceder 100)

Validação de Tarefas  
A tarefa será concluída automaticamente assim que a regra do Amazon EventBridge for formulada para encaminhar a solicitação ao destino apropriado. Além disso, você pode verificar seu progresso clicando no botão "Verificar meu progresso" na tela de detalhes do desafio.
