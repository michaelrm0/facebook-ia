from flask import Flask, request
from bot import Bot

import json
import os

#PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')
#PAGE_ACCESS_TOKEN = 'EAAGJKF6IdgcBAPvMCTGPZA7OlvmgqMHEj1rjkgSBXkZB1u2wl0iuZB2ROK76jlQFdBxQDw4OKjT6yaZA9MJQCZBaC2mZABSydKcM42YR1AuVh9DZAMmOTA7sEUOKXZARQbNXR2ZBd1iO4mZAAzACZAEbx4Jkx2nENjCh3l99Po35a3HF8jCqZBSKTqmB'
#PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')

def read_token():
    with open("token.txt", "r") as token:
        lineas = token.readlines()
        return lineas[0].strip()

def read_verify_token():
    with open("token_verificador.txt", "r") as verify_token:
        lineas = verify_token.readlines()
        return lineas[0].strip()

def read_mode():
    with open("mode.txt", "r") as mode:
        lineas = mode.readlines()
        return lineas[0].strip()

PAGE_ACCESS_TOKEN = read_token()
VERIFY_TOKEN = read_verify_token()
MODE = read_mode()

GREETINGS = ['hola', 'cómo estás', 'buenas']

app = Flask(__name__)

#Creamos la ruta
@app.route('/', methods = ['GET', 'POST'])
def webhook():
    global PAGE_ACCESS_TOKEN
    global VERIFY_TOKEN
    global MODE
    if request.method == 'GET':
        '''
        Necesitamos validar el token para que pueda haber un puente de
        enlace con messenger
        '''
        print(f"GET: {PAGE_ACCESS_TOKEN} - {VERIFY_TOKEN} - {MODE}")
        #VERIFY_TOKEN = 'HolaMundoCruel' 
        
        #MODE = 'subscribe'
        
        #VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
        #MODE = os.environ.get('MODE')        

        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        mode = request.args.get('hub.mode')


        if mode == MODE and token == VERIFY_TOKEN:
            print(token)
            print(challenge)
            print(mode)
            return str(challenge)            
        #devolvemos 200 en caso sea exitoso
        return '400'
    elif request.method == 'POST': 
        print(f"POST: {PAGE_ACCESS_TOKEN} - {VERIFY_TOKEN} - {MODE}")       
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