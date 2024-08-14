from flask import Blueprint, Flask, request
from Controllers.WikipediaController import handle_query
from Controllers.LLMmathController import handle_query
from Controllers.PyhtonreplController import handle_query
api_blue_print = Blueprint('api_blue_print', __name__)

@api_blue_print.route('/wikipedia', methods=['GET'])
def home():
    return handle_query(request)

@api_blue_print.route('/math', methods=['GET'])
def home():
    return handle_query(request)

@api_blue_print.route('/python', methods=['GET'])
def home():
    return handle_query(request)



