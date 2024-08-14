from flask import Flask
from Routes.Routes import api_blue_print  

app = Flask(__name__)

app.register_blueprint(api_blue_print)

if __name__ == "__main__":
    app.run(debug=True)
