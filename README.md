# Busca de CEP

## Descrição
Aplicação web desenvolvida em Python utilizando Flask para consulta de endereços a partir de um CEP.  
O sistema consome uma API externa e exibe informações como localidade, UF, bairro, logradouro, DDD, IBGE, entre outras.

## Funcionalidades
- Consulta de endereço a partir de um CEP
- Exibição de dados como:
  - Localidade / UF
  - Região
  - Bairro
  - Complemento
  - Logradouro
  - IBGE, GIA, DDD e SIAFI
- Interface web simples para entrada de dados

## Tecnologias utilizadas
- Python
- Flask
- Requests
- Flask-Migrate
- Flask-SQLAlchemy

## Executar
Siga os passos abaixo para executar o projeto localmente.

### Caso esteja utilizando sistemas Linux baseados em Debian:
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

Instale as dependências:
```
pip install -r requeriments.txt
```

Crie o banco:
```
flask db upgrade
```

Execute a aplicação:
```
python3 app.py
```

### Caso esteja utilizando sistemas Linux baseados em fedora:
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

Instale as dependências:
```
pip install -r requeriments.txt
```

Crie o banco:
```
flask db upgrade
```

Execute a aplicação:
```
python3 app.py
```

### Caso esteja utilizando sistemas Linux baseados em Arch:
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

Instale as dependências:
```
pip install -r requeriments.txt
```

Crie o banco:
```
flask db upgrade
```

Execute a aplicação:
```
python3 app.py
```

Acesse no navegador:

http://127.0.0.1:5000/


### Windows
Instale o Python em https://www.python.org/

Crie e ative um ambiente virtual:
```
python3 -m venv env
env\Scripts\activate.bat
```

Instale as dependências:
```
pip install -r requeriments.txt
```

Crie o banco:
```
flask db upgrade
```

Execute a aplicação:
```
python app.py
```

Acesse no navegador:

http://127.0.0.1:5000/

## Execução dos testes
Para a execução dos testes é necessário que o módulo **[Executar](#executar)** esteja concluído.  
Execução do pytest:
```
python3 -m pytest
```

## Observações
Caso ocorra erro relacionado à tabela `cep`, execute os comandos abaixo na pasta raiz do projeto:

Remover arquivos de migração:
- Linux:
```
rm -rf migrations
rm -rf instance
```

- Windows:
```
rmdir /s /q migrations
rmdir /s /q instance
```

Recriar as migrações:
```
flask db init
flask db migrate -m "initial tables"
flask db upgrade
```

## O que aprendi com este projeto
- Desenvolvimento de aplicações web com Flask
- Consumo de APIs externas
- Uso de banco de dados com SQLAlchemy
- Criação e gerenciamento de migrações
- Organização de um projeto backend em Python
