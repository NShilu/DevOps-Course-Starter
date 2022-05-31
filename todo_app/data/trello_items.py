from flask import session,Flask
import requests
import os
from todo_app.flask_config import Config
import json

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
    api_key = os.getenv('API_KEY')
    api_server_token = os.getenv('API_SERVER_TOKEN')
    cards_param = {'cards': 'open','key':api_key,'token':api_server_token}
    response = requests.get(f'https://trello.com/1/boards/{os.getenv("API_TRELLO_BOARDID")}/lists', params=cards_param)
    for my_list in response.json():
        for card in my_list['cards']:
           item = Item.from_trello_card(card, my_list)
           items.append(item)
    return items

def add_item(title):
    api_key = os.getenv('API_KEY')
    api_server_token = os.getenv('API_SERVER_TOKEN')
    cards_param = {'key':api_key,'token':api_server_token,'idList':os.getenv('API_ADDITEMLISTID'),'name':title}
    response=requests.post('https://api.trello.com/1/cards', params=cards_param)
    response.raise_for_status()
    
def complete_card(id):
    api_key = os.getenv('API_KEY')
    api_server_token = os.getenv('API_SERVER_TOKEN')
    cards_param = {'key':api_key,'token':api_server_token, 'idList':os.getenv('API_COMPLETECARDLISTID')}
    response=requests.put(f'https://api.trello.com/1/cards/{id}',params=cards_param)
    response.raise_for_status()


