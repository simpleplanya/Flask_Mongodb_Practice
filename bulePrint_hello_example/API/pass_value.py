from flask import Blueprint,request,jsonify,Response
import json

# Json_pass is object 
Json_pass = Blueprint('pass',__name__)

@Json_pass.route("/pass",methods=['POST'])
def get():
    content = request.get_json(force=True)
    return Response(json.dumps({"code":200,"message":content}),mimetype='application/jshon')



