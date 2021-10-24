from flask import Flask, render_template
# Importando a instância do flask
from flask_sqlalchemy import SQLAlchemy
# Importando a instância do SQL Alchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes