import os

from app_service import AppService
from db import Database
from flask import Flask, request

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db = Database(database=DB_NAME, host=DB_HOST,
              user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

app = Flask(__name__)
appService = AppService(database=db)

@app.route("/")
def home():
    primer_integrante = "Anthony Guevara"
    segundo_integrante = "Darío Espinoza"
    tercer_integrante = "Jerson Prendas"
    cuarto_integrante = "Marbel Brenes"
    texto = f"Trabajo de investigación, integrantes: \n\n \
            {primer_integrante} \n \
            {segundo_integrante} \n \
            {tercer_integrante} \n \
            {cuarto_integrante} \n"
    return texto

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return appService.get_tasks()