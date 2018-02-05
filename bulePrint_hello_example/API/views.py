from flask import Blueprint

blueprint = Blueprint('hello',__name__)
blueprint = Blueprint('teste',__name__)

@blueprint.route("/")

def hello():
    return "hello World"

@blueprint.route("/test")

def teste():
    return "test-area"
