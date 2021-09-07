import json

import requests
from django.http import HttpResponse
from django.views import View

from vk.models import Post

TG_TOKEN = ''
VK_ANSWER = ''
NEW_POST = 'wall_post_new'
TELEGRAM_URL = f'https://api.telegram.org/bot{TG_TOKEN}/'
CHAT_ID = ''
SEND_MESSAGE_TG = TELEGRAM_URL + "SendMessage"


def send_telegram(post):
    telegram_data = {
        'chat_id': CHAT_ID,
        'text': post.text
    }
    requests.post(SEND_MESSAGE_TG, data=telegram_data)


class VkToTg(View):
    def post(self, request):
        vk_message = json.loads(request.body.decode('utf8', errors='ignore'))
        if vk_message.get('type', False) == NEW_POST:
            new_post = Post(post_id=vk_message['object'].get('id', ''),
                            owner_id=vk_message['object'].get('owner_id', ''),
                            text=vk_message['object'].get('text', ''))

            new_post.save()
            send_telegram(new_post)
        return HttpResponse('ok')
