<<<<<<< HEAD
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_mail import Mail


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

bootstrap = Bootstrap()

db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    bootstrap = Bootstrap(app)
    login_manager.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)

    return app 
=======
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
db = SQLAlchemy()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
mail = Mail()
simple = SimpleMDE()
# instance of loginmanager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    # initializing application
    app = Flask(__name__)
   
    app.debug = True
     
    # creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # initializing flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    # Regestering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    # configure UploadSet
    configure_uploads(app,photos)
    return app
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
