import requests
import sys
from faker import Faker

ENDPOINT='https://desafiopython.jogajuntoinstituto.org/api/users/'

def generate_persona() -> dict:
	"""
	Gera uma persona fictícia com dados como nome de usuário, email, senha, telefone, endereço e CPF.

	Returns:
		dict: Um dicionário contendo os dados da persona.
	"""
	fake = Faker('pt_BR')
	persona: dict = {
    "username": fake.user_name(),
    "email": fake.email(),
    "password": fake.password(),
    "phone": fake.phone_number(),
    "address":fake.address(),
    "cpf":fake.cpf()
  }
	return persona

def register_user_by_api(persona: dict) -> dict:
	"""
    Registra a persona gerada na API.

    Args:
			persona (dict): Um dicionário contendo os dados da persona a ser registrada.

    Returns:
			dict: A resposta JSON da API se o registro for bem-sucedido.

    Ends:
			O programa com uma mensagem de erro se o registro não for bem-sucedido.
	"""
	response: requests.Response = requests.post(ENDPOINT , json=persona)
	if response.status_code == 201:
		print("Usuário criado com sucesso!")
		return(response.json())
	else:
		sys.exit("ERR: Houve um problema ao registrar o usuário")

def create_and_regiter_user() -> dict:
	"""
	Gera uma persona e a registra na API.

	Retorna:
		dict: Os dados da persona gerada.
	"""
	data = generate_persona() 
	register_user_by_api(data)
	return data

if __name__ == "__main__":
  print(create_and_regiter_user())