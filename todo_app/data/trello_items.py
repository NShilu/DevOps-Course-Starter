from flask import session,Flask
import requests
import os
from todo_app.flask_config import Config
import json

api_key = os.getenv('API_KEY')
api_server_token = os.getenv('API_SERVER_TOKEN')

class Item:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    @classmethod
    def from_trello_card(Item, card, list):
        return Item(card['id'], card['name'], list['name'])  

def get_items():
    items=[]
    cards_param = {'cards': 'open','key':api_key,'token':api_server_token}
    response = requests.get('https://trello.com/1/boards/621e24addce3fd2cedb1326e/lists', params=cards_param)
    for my_list in response.json():
        for card in my_list['cards']:
           item = Item.from_trello_card(card, my_list)
           items.append(item)
    return items

def add_item(title):
    
    cards_param = {'key':api_key,'token':api_server_token,'idList':'621e24addce3fd2cedb1326f','name':title}
    response=requests.post('https://api.trello.com/1/cards', params=cards_param)
    response.raise_for_status()
    
def complete_card(id):
    cards_param = {'key':api_key,'token':api_server_token, 'idList':'621e24addce3fd2cedb13271'}
    response=requests.put(f'https://api.trello.com/1/cards/{id}',params=cards_param)
    response.raise_for_status()


