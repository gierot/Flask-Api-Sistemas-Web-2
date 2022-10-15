import os

from flask import Flask
from . import db
from . import users
from . import cursos
from . import comentarios

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    app.register_blueprint(users.bp)
    app.register_blueprint(cursos.bp)
    app.register_blueprint(comentarios.bp)
    
    @app.route('/')
    def main():
        return 'Hello mom!'
    return app