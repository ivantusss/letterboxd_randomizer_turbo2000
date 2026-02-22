import random
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

    # 1. Выбор аккаунта
username = input('Enter Letterboxd username: ')

def page_reading(username, function_page):
    
        # 2. Отправка GET-запроса
    url = f'https://letterboxd.com/{username}/watchlist/page/{function_page}/'
    response = requests.get(url)

        # 3. Парсинг содержимого
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print("Ошибка при получении страницы")

            # 4. Извлечение данных
    data = [tag.get('data-item-name') for tag in soup.find_all('div')]
    if data:
        function_page_films = [film for film in data if not film == None] 
    else: function_page_films = []

    return function_page_films

    # 5. Извлечение фильмов со всех страниц
all_pages_films = []
    
for page in range(1,100):
    sec = [3,4,5,6,7,8,9,10]
    sleep(random.choice(sec))
    page_films = page_reading(username, page)
    if page_films == []: break
    elif page_films == all_pages_films: break
    else:
        print(page_films)
        all_pages_films += page_films

    # 6. Определение случайного фильма
print(random.choice(all_pages_films))
print(all_pages_films)

