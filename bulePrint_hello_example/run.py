from flask import Flask 
from API.views import blueprint
from API.pass_value import Json_pass
app = Flask(__name__)
app.register_blueprint(blueprint)
app.register_blueprint(Json_pass)

if __name__ == "__main__":
    app.run()
