from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # тут app это переменная
app.config.from_object(Config) # берем настройки из класса
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# нижний импорт известное решение, позволяющее избежать циклического импортаб , распространенной проблемы с приложениями Flask
from app import routes, models   # impo