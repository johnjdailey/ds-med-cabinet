# __init__.py



# Imports

from flask import Flask
from routes.GET_PUT_API import GET_PUT_API


# Create Flask app

def create_app():
    
    app = Flask(__name__)

    my_app = create_app()

    app.register_blueprint(GET_PUT_API)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
