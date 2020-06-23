#__init__.py



from flask import Flask
from API import API


def create_app():
    
    app = Flask(__name__)
    
    app.register_blueprint(API)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
