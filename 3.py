import requests
from Decorator2 import logger
path = 'hero.log'
@logger(path)
def hero_intelligence(heroes_list, link):
    data = link.json()
    dict = {}
    for hero in data:
        if hero['name'] in heroes_list:
            heroe_dict = {hero['name']: hero['powerstats']['intelligence']}
            intelligence_dict ={v: k for k, v in heroe_dict.items()}
            dict.update(intelligence_dict)
    return dict[max(dict)]


if __name__ == '__main__':
    list_ = ['Hulk', 'Thanos', 'Captain America']
    res = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    hero_intelligence(list_, res)