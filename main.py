from fastapi import FastAPI, Request

app = FastAPI()

def getIsRandomizeCommand(text: str):
    s = text.split(' ')
    if (len(s) != 2):
        return False, None

    command, username = s
    if (command != '/random'):
        return False, None

    return True, username

def processRandomCommand(text: str):
    s = text.split(' ')
    if (len(s) != 2):
      print('command has no username argument')
      return
    
    _, username = s
    print('received get random film command for user ' + username)

# TODO: add secret prefix after webhook path
@app.post('/webhook')
async def telegramWebhook(request: Request):
    body = await request.json()
    print(body)

    if 'message' in body and 'text' in body['message']:
      text: str = body['message']['text']
      print(text)

      if text.startswith('/random'):
        processRandomCommand(text)

    return {"ok": True}