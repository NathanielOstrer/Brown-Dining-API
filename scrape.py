from bs4 import BeautifulSoup
import requests

dining_halls = ['josiahs']

def get_menu_link(dining_hall):
    soup = BeautifulSoup(requests.get('https://dining.brown.edu/cafe/{}'.format(dining_hall)).text, features='html.parser')
    menu_link = soup.find_all("a", string='View/Print Weekly Menu')[0]['href']

    return menu_link

def get_menu(link):
    soup = BeautifulSoup(requests.get(link).text, features='html.parser')

    rows = soup.find_all('div', {'class': 'row'})

    for row in rows:
        row_name = row.find('div', {'class' : 'spacer', 'class' : 'day'}).text
        menu_items = [i.text for i in row.find_all('span', {'class' : 'weelydesc'})] #.rstrip().strip()

        print(row)
        print(len(menu_items), menu_items)



get_menu(get_menu_link(dining_halls[0]))

