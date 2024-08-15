from flask import Blueprint, Flask, request
from controllers.WikipediaController import handle_query as handle_query_wikipedia
from controllers.LLMmathController import handle_query as handle_query_math
from controllers.PyhtonreplController import handle_query as handle_query_python
from controllers.UserController import create
api_blue_print = Blueprint('api_blue_print', __name__)

@api_blue_print.route('/wikipedia', methods=['GET'])
def wikipedia():
    return handle_query_wikipedia(request)

@api_blue_print.route('/math', methods=['GET'])
def math():
    return handle_query_math(request)

@api_blue_print.route('/python', methods=['GET'])
def python():
    return handle_query_python(request)

@api_blue_print.route('/users', methods=['POST'])
def home():
    return create(request)

@api_blue_print.route('/users', methods=['GET'])
def get_user():
    return get_user(request)

@api_blue_print.route('/users', methods=['PUT'])
def update_user():
    return update_user(request)

@api_blue_print.route('/users', methods=['DELETE'])
def delete_user():
    return delete_user(request)


