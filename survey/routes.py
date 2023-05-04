from flask import jsonify, Blueprint,request
from decorators import mongo
survey = Blueprint("users", __name__, template_folder="templates")

@survey.route('/update_survey',methods=['POST'])
@mongo
def check_server(db):
    try:
        data = (request.json)
        db['surveys'].update_one(
        {"_id": data['uuid']},
        {"$set": data},
        upsert=True
        )
        return jsonify({'success': True})
    except Exception as E:
        print(E)
        return jsonify({'success': False})