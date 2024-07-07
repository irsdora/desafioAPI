import requests
from faker import Faker

ENDPOINT='https://desafiopython.jogajuntoinstituto.org/api/users/'


def create_user() -> dict:
  fake = Faker('pt_BR')
  data = {

    "username": fake.user_name(),
    "email": fake.email(),
    "password": fake.password(),
    "phone": fake.phone_number(),
    "address":fake.address(),
    "cpf":fake.cpf()
  }
  print(data["password"])
  return data
 

def register_user(data): 
   response = requests.post(ENDPOINT , json=data)
   print (response.json())


def main():
   data = create_user() 
   register_user(data)

main()