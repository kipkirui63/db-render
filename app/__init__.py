from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config  # Import the Config class from the config module

app = Flask(__name__)

# Set database configuration
app.config.from_object(Config)

db = SQLAlchemy(app)

def create_app():
    CORS(app, origins="*")
    
    # Import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
