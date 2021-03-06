from flask import Flask
from config import Config
from .authentication.routes import auth
from .site.routes import site
from flask_migrate import Migrate, migrate
from .models import db

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)

db.init_app(app)

migrate = Migrate(app,db)