from flask import Flask
import config

def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY = config.SECRET_KEY
    )

    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)

    from . import inputForm
    app.register_blueprint(inputForm.bp)

    from . import forwardToDestination
    app.register_blueprint(forwardToDestination.bp, url_prefix='/api/shorturl/')

    return app

