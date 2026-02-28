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
    req = await request.json()
    print(req)

    text = req.message.text
    print(text)

    isRandomizeCommand, username = getIsRandomizeCommand(text)
    if (isRandomizeCommand):
      print('received get random film command for user ' + username)

    return {"ok": True}