# API PYTHON 3 SIMPLES COM ARQUIVO JSON 
API Python 3 Simples com arquivo Json como fonte de dados.

A Api criada serve apenas para consulta de dados, não podendo adicionar, deletar ou alterar os dados, exerto se modificar o arquivo data.json. 

## Comandos para rodar o projeto
### Criar o ambiente virtual
```cmd
python3 -m venv venv
```
### Ativar ambiente virtual
- Windows
```cmd
venv\Scripts\activate
```
- Linux
```cmd
source venv/bin/activate
```
### Instalar pacotes a partir do arquivo requirements.txt
```cmd
pip install -r requirements.txt
```
### Rodar projeto
```cmd
python src/main.py
```

## Acessar a Api
- Para acessar todos os dados da api utilize a url: http://127.0.0.1:5000/api
- Para acessar um registro específico utilize a url: http://127.0.0.1:5000/api/1 > sendo o número 1 a id do item.

## Plugins Utilizados
- Flask
