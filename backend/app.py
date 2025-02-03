from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Book

app = Flask(__name__)

# Veritabanı URI ayarları
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Veritabanı bağlantısını başlat
db.init_app(app)

# Ana sayfa
@app.route('/')
def index():
    return "Kitap öneri sistemine hoş geldiniz!"

if __name__ == '__main__':
    app.run(debug=True)




