import requests
import json

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v2.6/me/'

class Bot(object):
    def __init__(self, access_token, api_url = FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    #Enviamos el mensaje
    def send_text_message(self, psid, message, messaging_type = "RESPONSE"):
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'messaging_type': messaging_type,
            'recipient': {
                'id': psid
            },
            'message': {
                'text': message
            }
        }

        params = {
            'access_token': self.access_token
        }

        self.api_url = self.api_url + 'messages'
        #Enviamos una solicitud de publicación
        response = requests.post(self.api_url,
                                 headers = headers,
                                 params = params,
                                 data = json.dumps(data))
        print(response.content)

bot = Bot('EAAGJKF6IdgcBAPvMCTGPZA7OlvmgqMHEj1rjkgSBXkZB1u2wl0iuZB2ROK76jlQFdBxQDw4OKjT6yaZA9MJQCZBaC2mZABSydKcM42YR1AuVh9DZAMmOTA7sEUOKXZARQbNXR2ZBd1iO4mZAAzACZAEbx4Jkx2nENjCh3l99Po35a3HF8jCqZBSKTqmB')
bot.send_text_message(3056506177784504,'Probando...')