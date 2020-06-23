#__init__.py



from flask import Flask
from Flask_API import Flask_API


def create_app():
    
    app = Flask(__name__)
    
    app.register_blueprint(Flask_API)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
