from flask import Flask, render_template
# Importando a instância do flask
from flask_sqlalchemy import SQLAlchemy
# Importando a instância do SQL Alchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '5f5e3ad8db84c9e5a33938ab'
db = SQLAlchemy(app)

from market import routes