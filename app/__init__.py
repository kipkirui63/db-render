# app.py
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://win_e_app_user:l789PbLqqTGNOzNjXMRXmAo42YbpHMcR@dpg-ckmijf2v7m0s73a4qko0-a.ohio-postgres.render.com/win_e_app'


db = SQLAlchemy(app)


def create_app(): 
    CORS(app)

    CORS(app, origins="*")

    # db.init_app(app)

    
    # add routes
    from app import routes

    return app
