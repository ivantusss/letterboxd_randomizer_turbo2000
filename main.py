import os

import requests
from fastapi import FastAPI, Request

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

def getIsRandomizeCommand(text: str):
    s = text.split(' ')
    if (len(s) != 2):
        return False, None

    command, username = s
    if (command != '/random'):
        return False, None

    return True, username

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def processRandomCommand(text: str, chat_id: str):
    s = text.split(' ')
    if (len(s) != 2):
      print('command has no username argument')
      return
    
    _, username = s
    print('received get random film command for user ' + username)
    send_message(chat_id, f'heyo {username}, we\'re working on this command')


# TODO: add secret prefix after webhook path
@app.post('/webhook')
async def telegramWebhook(request: Request):
    body = await request.json()
    print(body)

    if 'message' in body and 'text' in body['message']:
      text: str = body['message']['text']
      chatId = body['message']['chat']['id']
      print(text)

      if text.startswith('/random'):
        processRandomCommand(text, chatId)

    return {"ok": True}