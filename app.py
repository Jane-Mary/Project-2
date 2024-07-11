from flask import Flask
from flask_migrate import Migrate

from routes.authRoute import auth
from routes.designRoute import design
from routes.homeRoute import home

from config import db,SECRET_KEY

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = SECRET_KEY

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth,url_prefix='/auth')
app.register_blueprint(design,url_prefix='/')
app.register_blueprint(home,url_prefix='/')

if __name__ == '__main__':
     app.run(debug=True)


