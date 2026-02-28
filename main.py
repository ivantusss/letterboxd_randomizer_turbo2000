from fastapi import FastAPI

app = FastAPI()



# endpoint = url that takes some request and returns a response
@app.get("/hello")
async def root():
    return "hello world"

@app.get("/main")
async def root():
    print('got request on /main endpoint')
    return "second endpoint"