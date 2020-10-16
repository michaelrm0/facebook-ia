from flask import Flask, request
import json

PAGE_ACCESS_TOKEN = 'EAAGJKF6IdgcBAEj2EDnoIC49TZCLkmKL2Wgjl7rPSZAsOMocYRUhkPP9dK3ZCxmRGJkSEs2f1JtiXeTJOjADpTpuoEFIofZBHLU9VHCJIFKZCnUFmZBZBNLjDvg1JAvqSE50u8zZCjimklLg94KXkWrTIl0TSBTl6CRBI6QrS0senz51Trr5Df5W'
app = Flask(__name__)

#Creamos la ruta
@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        '''
        Necesitamos validar el token para que pueda haber un puente de
        enlace con messenger
        '''
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'secret':
            return str(challenge)
        #devolvemos 200 en caso sea exitoso
        return '400'
    else:        
        print(request.data)
        #Guardamos la información de fb en un json        
        dato = request.data
        data = json.loads(dato)
        #Guardamos los eventos de mensajería
        messaging_events = data['entry'][0]['messaging']
        #Entramos a todos los eventos
        for message in messaging_events:
            #Obtenemos el id del emisor
            user_id = message['sender']['id']
            '''
            Obtenemos el texto del emisor
            Ponemos el get debido a que el mensaje puede que sea 
            una imagen y puede que falle el código ya que sino 
            sería ['message']['text']
            '''
            text_input = message['message'].get['text']
            #El format sirve para poner los datos en las llaves
            print('Mensaje del usuario_ID {} - {}'.format(user_id, text_input))
        return '200'
        
if __name__ == '__main__':
    app.run(debug = True)    
    
'''
{
    "object":"page",
    "entry":
    [{
        "id":"106501624567068",
        "time":1602749549184,
        "messaging":
        [{
            "sender":
            {
                "id":"3056506177784504"
            },
            "recipient":
            {
                "id":"106501624567068"
            },
            "timestamp":1602749544338,
            "message":
            {
                "mid":"m_yUwR_aaYoRwc_ZaADAGX1PHsxe89Al1BEp0h_VAdMgkJaUfr1vzVsr_OtKuSuxeZbwfT05in4fq5qOvZPEM8Cw",
                "text":"jaja"
            }
        }]
    }]
}
'''