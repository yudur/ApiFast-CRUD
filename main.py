from fastapi import FastAPI
from pydantic import BaseModel

import mysql.connector

import os
from dotenv import load_dotenv

import re

load_dotenv()

class User(BaseModel):
    nome: str
    email: str | None = None
    telefone: str | None = None

app = FastAPI()




@app.post("/api/create_user/")
async def create_user(user: User):
    if len(user.nome) <= 0:
        return {
            "status": {
                "error": True,
                "code": 400,
                "type": "Bad Request",
                "message": 'the variable "nome" is invalid'
            }
        }
    elif len(user.nome.split()) <= 1:
        return {
            "status": {
                "error": True,
                "code": 400,
                "type": "Bad Request",
                "message": 'the variable "nome" must contain your last name'
            }
        }

    regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not user.email is None and not re.fullmatch(regex_email, user.email):
        return {
            "status": {
                "error": True,
                "code": 400,
                "type": "Bad Request",
                "message": 'invalid email'
            }
        }
    
    regex_telefone = re.compile(r'[0-9]{11}')
    if not user.telefone is None and not re.fullmatch(regex_telefone, user.telefone):
        return {
            "status": {
                "error": True,
                "code": 400,
                "type": "Bad Request",
                "message": 'invalid telefone'
            }
        } 
    
    try:
        db = mysql.connector.connect(
            user='root',
            password=os.getenv("PASSWORD_MYSQL"),
            host='127.0.0.1',
            database="crudfastapi"
        )
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO users (nome, email, telefone) VALUES ('{user.nome}', '{user.email}', '{user.telefone}')")
        db.commit()

        return {
            "status": {
                "error": False,
                "code": 200,
                "type": "success",
                "message": "user created successfully"
            },
            "data": user
        }
    except Exception as error:
        return {
            "status": {
                "error": True,
                "code": 400,
                "type": "Bad Request",
                "message": error
            }
        }


def read_user():
    pass

def update_user():
    pass

def delete_user():
    pass