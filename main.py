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

@app.post('/webhook')
async def telegramWebhook(request: Request):
    body = await request.json()
    print(body)

    try:
      text = body['message']['text']
    except Exception as err:
      print(err)
      return {'ok': 'True'}

    print(text)

    isRandomizeCommand, username = getIsRandomizeCommand(text)
    if (isRandomizeCommand):
      print('received get random film command for user ' + username)

    return {"ok": True}