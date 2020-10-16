from flask import Flask, request
from bot import Bot

import json

PAGE_ACCESS_TOKEN = 'EAAGJKF6IdgcBACNkGj6ZBLoCpXqMjYAF1AIi5vV56UZBrUt4KsUD6XPRFLS3ZBjjkxgTgDHr1rmXQOhqFAMyO8qcOKtc7YIUSZBtQJ456ATmHQtLU7nlYCwZCwf1kYnijZBZA7FntujVG4X6W0UXfEhesVooePM2ZBuHE4SzPgNYSI33yoZBkx5Cn'

GREETINGS = ['hola', 'cómo estás', 'buenas']

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
        #Guardamos la información de fb en un json        
        print(request.data)
        data = json.loads(request.data)
        #Guardamos los eventos de mensajería
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
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
            text_input = message['message'].get('text')
            response_text = 'Me encuentro en proceso de aprendizaje 😒'
            #Si el texto ingresado forma parte del array GREETINGS mostrar los sgte
            if text_input in GREETINGS:
                response_text = 'Hola. Bienvenido te habla la computadora, decir aua 😁'
            #El format sirve para poner los datos en las llaves
            print('Mensaje del usuario_ID {} - {}'.format(user_id, text_input))
            #bot.send_text_message(user_id, 'Procesando...')
            bot.send_text_message(user_id, response_text)

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