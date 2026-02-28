import csv
import random

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
}
   

def main(): 
    username = input('Enter Letterboxd username: ')
    print('Wait a little...')
    print('_____________________')

    def page_reading(username, page_number):
        
            # 1. Sending GET-request
        url = f'https://letterboxd.com/{username}/watchlist/page/{page_number}/'
        response = requests.get(url,headers=headers)

            # 2. Content parsing
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        else: print("Ошибка при получении страницы")
        
            # 3. Data extraction
        data = [tag.get('data-item-name') for tag in soup.find_all('div')]
        if data:
            function_page_films = [film for film in data if not film == None] 
        else: function_page_films = []

        return function_page_films

        # 4. Collecting all films
    all_pages_films = []
        
    for page in range(1,100):
        page_films = page_reading(username, page)
            
        if page_films == (all_pages_films or []):
            print(all_pages_films)
            break
        else: all_pages_films += page_films

        # 5. Finding 'Thursday' movie because it is cool film
    if 'Thursday (1998)' in all_pages_films:
        print('Thursday (1998)\nThere is no more choice for you')
        
        # 6. Choosing random film
    else:
        random_films = [random.choice(all_pages_films) for film in range(5)]
        choice_num = 0
        
        while choice_num < len(random_films):
            print(random_films[choice_num])
            print('_____________________')
            film_choice = input('Show next film? - ')
            
            if film_choice == 'yes' or 'Yes' or 'YES':
                choice_num += 1
            else: break
            
        if choice_num == len(random_films):
            print('Try to finally select one of these films')

main()