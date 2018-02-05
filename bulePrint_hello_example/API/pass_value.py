from flask import Blueprint,request,jsonify,Response

# Json_pass is object 
Json_pass = Blueprint('pass',__name__)

@Json_pass.route("/pass",methods=['POST'])
def get():
    content = request.get_json(force=True)
    return jsonify({"code":200,"message":content})


