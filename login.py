import requests
import json
import sys
import usuario as user

ENDPOINT='https://desafiopython.jogajuntoinstituto.org/api/users/login/'

def get_registered_user() -> dict:
  return user.create_and_regiter_user()

def login_by_api(email: str, password: str) -> dict: 
	"""
	Realiza login na API com o email e senha fornecidos.

	Args:
			email (str): O email do usuário.
			password (str): A senha do usuário.

	Returns:
			dict: A resposta JSON da API se o login for bem-sucedido.

	Exit:
			O programa com uma mensagem de erro se o login não for bem-sucedido.
	"""
	response: requests.Response = requests.post(ENDPOINT, json={"email": email,"password": password})
	if response.status_code == 200:
		print("Login realizado com sucesso!")
		return response.json()
	else:
		sys.exit("ERR: Houve um problema ao registrar o usuário")

def save_to_file(data: dict) -> None:
	"""
	Salva os dados fornecidos em um arquivo JSON.

	Args:
			data (dict): Os dados a serem salvos no arquivo.

	Raises:
		FileNotFoundError: Se o arquivo/PATH a ser salvo não for encontrado
		IOError: Se houver algum erro durante o salvamento do arquivo
	"""
	PATH = "token.json"
	try: 
		with open(PATH, 'w') as file:
			json.dump(data, file, ensure_ascii=True)
			print(f"Acesso salvo com sucesso em {PATH}")
	except FileNotFoundError:
		print(f"Arquivo {PATH} não encontrado...")
	except IOError:
		print(f"Não foi possível escrever em {PATH}")
   
def main() -> None:
   user = get_registered_user() 
   token = login_by_api(user['email'], user['password'])
   save_to_file(token)

if __name__ == "__main__":
   main()