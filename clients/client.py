from ast import Raise
import requests
from getpass import getpass
import json


def log_user():
        username = input('  [*] Username: ')
        password = getpass('  [*] Password: ')
        return username, password

def login():
    print('')
    print('[+] Welcome to the HedgeFund Manager API')
    print('')
    print('[+] Login')
    while True:
        username, password = log_user()
        print('')
        token = ''
        auth_endpoint = 'http://127.0.0.1:8000/hfma/auth/'
        auth_response = requests.post(auth_endpoint, json={"username":username, "password":password})
        if auth_response.status_code == 200:
            token = auth_response.json()['token']
            break
        else:
            print('[-] Incorrect Login, try again. ')
    
    header = { "Authorization": f"Token{token}" }
    return header

    
def desired_action():
    print('')
    print('[+] Select Action:\n')
    print('     [1] Create')
    print('     [2] Read ')
    print('     [3] Update ')
    print('     [4] Delete ')
    print('')
    action = input('[*] Action: ')
    id = None
    if action != 1:
        id = input('[*] Specify ID: (type -1 for overall lookup when reading): ')
    print('\n')
    return action, id

def desired_model():
    print('[+] Select Model:\n')
    print('     [1] Asset')
    print('     [2] Client ')
    print('     [3] Employee ')
    print('     [4] ControlPanel ')
    print('')
    model = input('[*] Model: ')
    print('\n')
    return model

def action_performer(action, model):
    lookup_model = ''
    crud_method = ''
    endpoint = ''
    if model == '1':
        lookup_model = 'asset'
    elif model == '2':
        lookup_model = 'client'
    elif model == '3':
        lookup_model = 'employee'
    elif model == '4':
        lookup_model = 'controlpanel'
    else:
        print('[-] Enter a valid input')
        Raise(Exception)

    if action[0] == '1': # Create
        crud_method = 'create'
        endpoint =  f'http://127.0.0.1:8000/hfma/{lookup_model}/{crud_method}/'
    elif action[0] == '2': # Read
        if action[1] == '-1':
            endpoint = f'http://127.0.0.1:8000/hfma/{lookup_model}/'
        else:
            endpoint = f'http://127.0.0.1:8000/hfma/{lookup_model}/{action[1]}'
    elif action[0] == '3': # Update
        crud_method = 'update'
        endpoint = f'http://127.0.0.1:8000/hfma/{lookup_model}/{action[1]}/{crud_method}/'
    elif action[0] == '4':
        crud_method = 'delete'
        endpoint = f'http://127.0.0.1:8000/hfma/{lookup_model}/{action[1]}/{crud_method}/'
    # print(endpoint)
    return endpoint

def main():
    header = login()
    while True:
        action = desired_action()
        model = desired_model()
        endpoint = action_performer(action, model)
        if action[0] == '1': # Create
            data = input('[*] JSON Input Create: ')
            json_data = json.loads(data)
            r = requests.post(endpoint, headers=header, json=json_data)
            print(r.status_code)
        elif action[0] == '2': # Read
            r = requests.get(endpoint, headers=header)
            print(r.json())
        elif action[0] == '3': # Update
            data = input('[*] JSON Input Update: ')
            json_data = json.loads(data)
            r = requests.put(endpoint, headers=header, json=json_data)
            print(r.status_code)
        elif action[0] == '4':
            r = requests.delete(endpoint, headers=header)
            print(r.status_code)
        

main()