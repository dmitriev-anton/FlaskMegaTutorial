from flask import Flask
app = Flask(__name__) # тут app это переменная
# нижний импорт известное решение, позволяющее избежать циклического импортаб , распространенной проблемы с приложениями Flask
from app import routes # impo