# Desafio Final: API Instituto Joga Junto 💛🔆
O objetivo deste desafio é testar os conhecimentos que o
squad adquiriu sobre:
- Github
- Python
- API

## Desafio 🎯
1. O squad deverá criar um usuário no seguinte endpoint `https://desafiopython.jogajuntoinstituto.org/api/users/`

2. Em seguida, deve fazer login com o usuário criado no endpoint `http://desafiopython.jogajuntoinstituto.org/api/users/login/`

3. Deve salvar o JSON que receber de resposta.


## Estrutura do JSON (User) 📦
 **O JSON de criar usuário conta com a estrutura:**
```json
{
    "username": "user",
    "email": "email@email.com",
    "password": "password",
    "phone": "123456789",
    "address": "123 Main St, City, Country",
    "cpf": "000.000.000-00"
}
```


## Estrutura do JSON (Login) 📦
**O JSON de login conta com a estrutura:**
```json
{
    "email": "email@email.com",
    "password": "password"
}
```
# Pré-requisitos 📋
- [Python 3.x](https://www.python.org/downloads/) (Eu utilizei a versão `3.11.2` enquanto desenvolvia esse projeto).

## Virtual Environment 🌲
Execute `python -m venv venv` para criar um ambiente virtual:
```bash
python -m venv venv
```

### Ative o ambiente virtual:

- Windows

```bash
venv\Scripts\activate
```
- Linux/MacOs
  
```bash
venv/bin/activate
```

## Instalação 🏗️
Instale todos os requisitos:
```bash
pip install -r requirements.txt
```

## Execute o programa ⚙️
Estando na pasta raíz do projeto, rode o arquivo `login.py` com o comando:
```bash
python login.py
```
Caso tenha sucesso, será gerado o arquivo `token.json` na pasta raíz.

## Apoie o projeto 🙌

Se você quiser apoiar o projeto, deixe uma ⭐.

___

Made with ❤️ by Squad 4.
