## Idea-WebAPI - FastAPI Project
Idea-WebAPI is a RESTful API built using FastAPI, PostgreSQL, and SQL Alchemy ORM model. It offers a robust and scalable backend for web applications.

The API is secured with authentication and authorization protocols that ensure data privacy and security. Users can vote, create, update, and delete posts. These functionalities are protected with secure endpoints.

The project also includes an automated database migration feature using Alembic and Pydantic models. This feature streamlines the development process, making it more efficient.

With Idea-WebAPI, developers can build scalable web applications with a secure backend that enables users to perform various actions while ensuring their data is kept safe.


## Installation and Setup in local environment   

> Clone the repository follow the following steps

```bash
$ git clone https://github.com/chirag4242/Idea-WebAPI.git

$ cd Idea-WebAPI 
```
Install all pip modules from `requirements.txt` 
> Run following command to install all the modules
```bash 
$ pip install -r requirements.txt
```
> Create .env file 
```bash 
$ pip install python-dotenv
```
> In .env file add the requried credentials and information please refer `config.py`file at `Idea-WebAPI/app/config.py`
> Run following command to start the application 
```bash
$ uvicorn Main:app --reload
```
>`--reload`: make the server restart after code changes. Only do this for development. 

#### Setup information 
- Required to create database with postgres and configure according naming in the application 
- Don't need to create tables as ORM model with sqlalchemy and alembic - `automate` this step 
- If you stuck into somewhere or get error please create the issue in issues section I would be happy to help you.

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=flat-square&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![JWT](https://img.shields.io/badge/JWT-black?style=flat-square&logo=JSON%20web%20tokens)

## More Information 
- Looking forward to work on front-end using this web API. 
- Please feel free to contact me or contribute in this project. 

## Author and Social

[![chirag42](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/chirag42/) 
[![@chirag4242](https://img.shields.io/badge/GitHub-181717.svg?style=flat-square&logo=GitHub&logoColor=white)](https://www.github.com/chirag4242)
[![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=flat-square&logo=firefox&logoColor=#FF7139)](https://cio-app.herokuapp.com/)
[![Projects](https://img.shields.io/badge/Projects%20Site-4285F4?style=flat-square&logo=GoogleChrome&logoColor=white)](https://sites.google.com/view/chiragpatil/home)
