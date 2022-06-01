from operator import contains
import string
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests
import os
import json

@pytest.fixture
def client():
# Use our test integration config instead of the 'real' version
 file_path = find_dotenv('.env.test')
 load_dotenv(file_path, override=True)
# Create the new app.
 test_app = app.create_app()
# Use the app to create a test_client that can be used in our tests.
 with test_app.test_client() as client:
  yield client

def test_index(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
  monkeypatch.setattr(requests, 'get', get_lists_stub)
  response = client.get('/')
  print(response.data)
  assert response.status_code == 200
  assert response!=''
  assert 'Test card' in response.data.decode()


class StubResponse():
  def __init__(self, fake_response_data):
   self.fake_response_data = fake_response_data

  def json(self):
   return self.fake_response_data

  def raise_for_status(self):
    pass


   
def get_lists_stub(url,params):
  test_board_id = os.environ.get('API_TRELLO_BOARDID')
  fake_response_data = None
  if url == f'https://trello.com/1/boards/{test_board_id}/lists':
    fake_response_data = [{
     'id': '123abc',
     'name': 'To Do',  
     'cards': [{'id': '456', 'name': 'Test card'}]
    }]
    
  return StubResponse(fake_response_data)

def test_addItem(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
  monkeypatch.setattr(requests, 'post', add_cards_stub)
  response = client.post('/addItem?123')
  assert response!=''
  assert response.status_code == 302
  

def add_cards_stub(url, params):
    test_board_id = os.environ.get('API_TRELLO_BOARDID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/cards':
      fake_response_data = {
        'id': 'abcd',
        'name': '123',
        'idBoard':'Test',
        'idList':'TestList'
      }
    
    return StubResponse(fake_response_data)