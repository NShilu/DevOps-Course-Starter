from flask import session, Flask
import requests
import dotenv 
import os

def get_items():
    dotenv.load_dotenv()
    board_id = os.getenv('API_TRELLO_BOARDID')
    api_key=os.getenv('API_KEY')
    api_server_token=os.getenv('API_SERVER_TOKEN')
    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {
        "key": api_key,
        "token": api_server_token,
        "cards":"open"
    }

    response = requests.get(reqUrl, params=params)
    response_json= response.json()
    cards = response_json[0]['cards']
    return cards
    