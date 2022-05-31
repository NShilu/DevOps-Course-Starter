import os
from threading import Thread
from urllib import response
import requests
import pytest
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

file_path = find_dotenv('.env')
load_dotenv(file_path, override=True)
api_key = os.getenv('api_key')
Consumer_Secret = os.getenv('CONSUMER_SECRET')
api_server_token = os.getenv('api_server_token')


auth_params = {'key':api_key,'token':api_server_token}


def create_trello_board(name):
    response=requests.post("https://api.trello.com/1/boards/?name="+name,params=auth_params)
    response_data = response.json()
    new_board_id=response_data["id"]
    return new_board_id

def get_todo_list_id(board_id):
    response = requests.get("https://trello.com/1/boards/"+board_id+"/lists", params=auth_params)
    response_data=response.json()
    for list in response_data:
       if list['name']=='To Do':
         todo_list_id = list['id']
    return todo_list_id   

def delete_trello_board(board_id):
    response=requests.delete("https://api.trello.com/1/boards/"+board_id,params=auth_params)
    return

@pytest.fixture(scope="module")
def driver():
 with webdriver.Chrome() as driver:
  yield driver

@pytest.fixture
def app_with_temp_board():
 file_path = find_dotenv('.env')
 load_dotenv(file_path, override=True)
  
# Create the new board & update the board id environment variable
 name = "TempBoard" 
 board_id = create_trello_board(name)
 os.environ['API_TRELLO_BOARDID'] = board_id
 todo_list_id = get_todo_list_id(board_id)
 os.environ['API_ADDITEMLISTID'] = todo_list_id
# construct the new application 
 application = app.create_app()
# start the app in its own thread.
 thread = Thread(target=lambda: application.run(use_reloader=False))
 thread.daemon = True
 thread.start()
 yield application
# Tear Down
 thread.join(1)
 delete_trello_board(board_id)



def test_task_journey(driver,app_with_temp_board):
     driver.get('http://localhost:5000/')
     assert driver.title == 'To-Do App'     

 

def test_app_addItem(driver,app_with_temp_board):
     driver.get('http://localhost:5000/')
     title_field = driver.find_element(By.ID,'title')
     title_field.send_keys("AppTesting8")
     submit_button = driver.find_element(By.ID,'AddValue')
     submit_button.click()
     assert len(driver.find_elements(By.XPATH,"//*[contains(text(), 'AppTesting8')]"))>0


