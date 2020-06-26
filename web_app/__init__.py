# __init__.py



# Imports

from flask import Flask
from web_app.routes.Directory import Directory
from web_app.routes.ParseURL import ParseURL
from web_app.routes.API import API


# Create Flask app

def create_app():
    
    # Instantiate the Flask app

    app = Flask(__name__)

    # Register blueprints

    app.register_blueprint(Directory)
    app.register_blueprint(ParseURL)
    app.register_blueprint(API)
    
    return app

# Create app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
