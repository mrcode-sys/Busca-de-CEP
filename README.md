# Busca De CEP

Esse é um projeto que fiz apenas para aprendizado para fazer buscas de CEP. Para usar-lo basta iniciar o arquivo app.py abrir o site http://127.0.0.1:5000/, informar um CEP, clicar em "Ir" e ele retornará Localidade/uf, Região, Bairro, Complemento, Logradouro, IBGE, GIA, DDD e siafi da localização informada
## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Para executar esse projeto será necessário o python e importar essas bibliotecas:
```
flask
requests
flask_Migrate
flask_sqlalchemy
```

### 🔧 Instalação
#### Caso esteja utilizando sistemas Linux baseados em Debian:
Instalar Python 3:
```
sudo apt update
sudo apt install python3
```
Instalar pip:
```
sudo apt install python3-pip
```
Criar e iniciar ambiente virtual:
```
python3 -m venv env
source env/bin/activate
```
#### Caso esteja utilizando sistemas Linux baseados em fedora:
Instalar Python 3:
```
sudo dnf install python3
```
Instalar pip:
```
sudo dnf install python3-pip
```
Criar e iniciar ambiente virtual:
```
python3 -m venv env
source env/bin/activate
```
#### Caso esteja utilizando sistemas Linux baseados em Arch:
Instalar Python 3:
```
sudo pacman -Syu
sudo pacman -S python
```
Instalar pip:
```
sudo pacman -S python-pip
```
Criar e iniciar ambiente virtual:
```
python3 -m venv env
source env/bin/activate
```
#### Caso esteja utilizando sistemas Windows:
Para instalar o python e o pip consulte o site https://www.python.org/

Criar e iniciar ambiente virtual:
```
python3 -m venv env
env\Scripts\activate.bat
```
#### Instalação das bibliotecas:
```
pip install flask requests flask_Migrate flask_sqlalchemy
```
Após isso será possível executar o app.py com esse comando na pasta raiz do projeto:
```
python3 app.py
```
ou, caso não funcione
```
python app.py
```
Caso ocorra um erro à falta da tabela cep, execute:
##### Linux:
Na pasta raiz do projeto:
```
rm -rf migrations
rm -rf instance
```
Ou remova os arquivos via interface
##### Windows:
```
rmdir /s /q "migrations"
rmdir /s /q "instance"
```
Ou remova os arquivos via interface
```
flask db init
flask db migrate -m "initial tables"
flask db upgrade
```
Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

## ✒️ Autor

* **mrcode-sys** - [mrcode-sys](https://github.com/mrcode-sys)
