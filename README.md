# IGS---Django-Coding-Tes

## Configuração
Acesse /IGS-Software-Manager/IGS-Employee e configure o acesso a um banco de dados postgres:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'IGS_Employee',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 'post',
        }
    }

Crie um SuperUser para acessar a área de administrador

    python manage.py createsuperuser


## Instalação
É necessário uma venv com python > 3.7 para a instalação correta das dependências;
    
    pip install requirements.txt


## Rodando o aplicativo

    python manage.py runserver

# REST API

Exemplos de utilização da REST API

## Listar Funcionários

    curl --location --request GET 'http://localhost:8000/get_employees' \
    --header 'Accept: application/json'

### Response

    [
        {
            "model": "employees.employee",
            "pk": 1,
            "fields": {
                "name": "teste",
                "email": "teste@gmail.com",
                "department": 1
            }
        },
        {
            "model": "employees.employee",
            "pk": 2,
            "fields": {
                "name": "teste1",
                "email": "teste1@gmail.com",
                "department": 1
            }
        },
    ]

## Listar Funcionário

    curl --location --request GET 'http://localhost:8000/get_employees?id=1' \
    --header 'Accept: application/json'

### Response

    [
        {
            "model": "employees.employee",
            "pk": 1,
            "fields": {
                "name": "teste",
                "email": "teste@gmail.com",
                "department": 1
            }
        }
    ]

## Criar Funcionário

    curl --location --request GET 'http://localhost:8000/create_employee?name=teste3&email=teste3@gmail.com&department=1' \
    --header 'Accept: application/json' 

### Response

    [
        {
            "model": "employees.employee",
            "pk": 3,
            "fields": {
                "name": "teste3",
                "email": "teste3@gmail.com",
                "department": 1
            }
        }
    ]

## Deletar Funcionário

    curl --location --request GET 'http://localhost:8000/delete_employee?id=3' \
    --header 'Accept: application/json' 

### Response 

    {
        "id": "3"
    }


