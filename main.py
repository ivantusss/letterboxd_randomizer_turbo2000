from fastapi import FastAPI, Request

app = FastAPI()



# endpoint = url that takes some request and returns a response
@app.get("/hello")
async def root():
    return "hello world"

@app.get("/main")
async def root():
    print('got request on /main endpoint')
    return "second endpoint"

@app.post('/webhook')
async def telegramWebhook(request: Request):
    update = await request.json()

    # process update
    print(update)

    return {"ok": True}