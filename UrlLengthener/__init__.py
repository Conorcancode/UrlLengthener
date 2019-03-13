from flask import Flask
import config

def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY = config.SECRET_KEY
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def hello():
        return "Hello, World!"

    from . import redirect
    app.register_blueprint(redirect.bp)

    return app

