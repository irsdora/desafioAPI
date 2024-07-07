import requests
import json 

ENDPOINT='https://desafiopython.jogajuntoinstituto.org/api/users/login/'

def create_user() -> dict:
  
  data = {

    
    "email": "maria61@example.com",
    "password": "9(2KayXpXf"
  }
  return data
 

def register_user(data): 
   response = requests.post(ENDPOINT , json=data)
   print(response.json())
   savetofile(response.json())

def savetofile(data):
 with open('token.json', 'w') as file:
    json.dump(data, file, ensure_ascii=True)
   

def main():
   data = create_user() 
   register_user(data)


main()