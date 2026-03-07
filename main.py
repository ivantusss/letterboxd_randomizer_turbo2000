import os

import requests
from fastapi import FastAPI, Request

import random
from bs4 import BeautifulSoup


BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
}
   
def page_reading(username, page_number):
    # 1. Sending GET-request
    url = f'https://letterboxd.com/{username}/watchlist/page/{page_number}/'
    response = requests.get(url,headers=headers)
    print(f'Making a request to get {username}\'s {page_number} wl page')

    # 2. Content parsing
    if response.status_code != 200:
        print('Error while getting letterbox wathchlist', url, response);
        return True, None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Data extraction
    data = [tag.get('data-item-name') for tag in soup.find_all('div')]
    if data:
        function_page_films = [film for film in data if not film == None] 
    else: function_page_films = []

    return False, function_page_films

def getWatchlist(username: str):
    all_pages_films = []
    
    for page in range(1,100):
        isError, page_films = page_reading(username, page)

        if isError:
            return True, None
            
        if page_films == []:
            break
        else: 
            all_pages_films += page_films
    
    return False, all_pages_films

def chooseRandomFilm(watchlist: list):
    if 'Thursday (1998)' in watchlist:
        return 'Thursday (1998)'
        
    random_film = random.choice(watchlist)
    return random_film

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
    isError, watchlist = getWatchlist(username)

    if isError:
        send_message(chat_id, 'There was an error, please try again later')
        return

    random_film = chooseRandomFilm(watchlist)

    send_message(chat_id, random_film)

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
