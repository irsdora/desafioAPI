# Desafio Final: API Instituto Joga Junto 💛🔆

<div align="center">
  <picture>
    <source srcset="https://www.jogajuntoinstituto.org/image/Logo_about.png" media="(prefers-color-scheme: light)">
    <img title="Instituto Joga Junto" alt="Instituto Joga Junto" href="https://www.jogajuntoinstituto.org/" src="https://github.com/rodrigomolter/qa-institutojogajunto/assets/57466763/acf43fcb-f91a-450d-9291-90b479b07064" width="400px">   
  </picture>
</div>
<br>

O objetivo deste desafio é testar os conhecimentos que o
squad adquiriu sobre:
- Github
- Python
- API

# Desafio 🎯
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

# Resolução ✔️
Foram criados dois arquivos para encapsulamento da resolução dos problemas: `usuario.py` e `login.py`.

**Usuario** é responsável pela criação de uma persona - baseado no JSON acima - e o cadastro dessa persona na API.

**Login** é responsável por efetuar a autenticação do usuário criado em `usuario` e armazenar a resposta com o *token JWT* e o *refresh token* em um arquivo chamado `token.json`.
>[!TIP]
> O arquivo `token.json` esta no `.gitignore` e por isso não é versionado ao Github.

Abaixo deixo os requisitos e passo-a-passo caso deseje executar localmente.

## Pré-requisitos 📋
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
