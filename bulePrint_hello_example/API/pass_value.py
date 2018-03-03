from flask import Blueprint,request,jsonify,Response
import json
from db import get_db
from bson.json_util import dumps

# Json_pass is object 
Json_pass = Blueprint('pass',__name__)

@Json_pass.route("/pass",methods=['POST'])
def get():
    content = request.get_json(force=True)
    return Response(json.dumps({"code":200,"message":content}),mimetype='application/jshon')

@Json_pass.route("/show",methods =['POST'])
def show():    
    TestDb = get_db()
    x = TestDb.testData.find()
    #print (list(x))
    content = request.get_json(force=True)
    return dumps(list(x),ensure_ascii=False) 









