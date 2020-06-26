# __init__.py



# Imports

from flask import Flask
from web_app.routes.Directory import Directory
from web_app.routes.API import API


# Create Flask app

def create_app():
    
    app = Flask(__name__)

    app.register_blueprint(Directory)
    app.register_blueprint(API)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
