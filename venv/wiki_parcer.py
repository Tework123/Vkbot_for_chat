import requests
from bs4 import BeautifulSoup
import lxml


def wiki_parcer():
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    random_page = soup.find(id="mw-navigation").find_all(class_='vector-menu-content')

    for i in random_page:
        # if i.find(class_='vector-menu-content-list') != None:
        #     if i.find(class_='vector-menu-content-list').find('li') != None:
        a = i.find(class_='vector-menu-content-list').find_all('li')
        for j in a:
            if j.get('id') == 'n-randompage':
                result = f"https://ru.wikipedia.org/{j.find('a').get('href')}"
    return result