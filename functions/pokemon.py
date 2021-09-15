import requests
from bs4 import BeautifulSoup

def pokemon_weakness(poke_name):
    content = requests.get("https://www.pokemon.com/us/pokedex/" + poke_name).text
    soup = BeautifulSoup(content, 'lxml')
    try:
        data = soup.find_all('div', {"class": "dtm-weaknesses"})
        clean_data = data[0].text.split(' ')
        weakness = []
        for i in clean_data:
            if i != '' and i != '\n':
                weakness += i
        t = ''
        for i in weakness:
            if i.isalpha():
                t += i
            else:
                if t != '':
                    weakness.append(t)
                    t = ''
        final_weekness = []
        for i in weakness:
            if len(i) > 2 and i != 'Weaknesses':
                final_weekness.append(i)

        return final_weekness
    except TypeError:
        return "check the spelling of the pokemon"
