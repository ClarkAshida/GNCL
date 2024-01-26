# GNCL, Gerenciador de Notícias do ContestLink

![Django](https://img.shields.io/badge/Django-3.0%2B-brightgreen)
![MySQL](https://img.shields.io/badge/MySQL-5.7%2B-blue)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.0%2B-purple)
![jQuery](https://img.shields.io/badge/jQuery-3.5%2B-blueviolet)
![Crispy Forms](https://img.shields.io/badge/Crispy%20Forms-1.12%2B-green)

## Description

GNCL is the News Manager for ContestLink, a CRUD system for managing news to be displayed on the "ContestLink" news portal. Additionally, it allows the management of employees responsible for publishing new articles within the system. This application is developed with Django on the backend, following the MVT (Model-View-Template) design pattern, using MySQL as the database, and employing HTML, CSS, JavaScript, Bootstrap, jQuery, and Crispy Forms on the frontend to create a user-friendly interface.

## Features

- Create, view, edit, and delete news within the system.
- Create, view, edit, and delete employees within the system.
- User authentication to manage the platform.
- Messaging and feedback system for users.
- Filtering and search functionality for easy discovery of news and employees.
- Pagination system for handling a large number of records.

## Requirements

- Django 3.0 or higher.
- Crispy Forms 1.12 or higher.
- Crispy Forms Bootstrap integration.
- MySQL 5.7 or higher.
- Bootstrap 4.0 or higher.
- jQuery 3.5 or higher.

## Installation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ClarkAshida/GNCL
   cd GNCL
   ```

2. Abra o arquivo `settings.py` no diretório `ContestLink` e insira as informações do seu banco de dados no bloco `DATABASES`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'mysql.connector.django',
           'NAME': 'seu_nome_de_banco',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

Substitua `'seu_nome_de_banco'`, `'seu_usuario'` e `'sua_senha'` pelos detalhes do seu banco de dados MySQL.

3. Ensure you have a MySQL database set up and run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser to access the system as an administrator:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up a username, email address, and password.

5. Start the server:

   ```bash
   python manage.py runserver
   ```

Access the system as an administrator at [http://localhost:8000/accounts/login](http://localhost:8000/accounts/login) using the credentials of the superuser created.

## Next Updates
In the upcoming releases of this project, the plan is to implement user permission levels, including roles such as news authors, writers, and administrators. Additionally, the next phase of the project involves completing the ContestLink news portal to consume the data published on GNCL. These additions aim to provide a more comprehensive and personalized experience for users, enabling finer control over the content of the portal and its contributions.

## Contributors

- I appreciate all the wonderful people who contributed to this project!:

- [IohanaViterbino](https://github.com/IohanaViterbino)
- [AlanFernandesXavier](https://github.com/AlanFernandesXavier)

---
