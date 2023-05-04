from flask import jsonify, Blueprint,request,render_template,send_from_directory
from decorators import mongo
import os

survey = Blueprint("survey", __name__, template_folder="templates",static_folder="build/static")

@survey.route('/update_survey',methods=['POST'],)
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
    
@survey.route('/seller_intake_survey')
def seller_intake_survey():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(current_dir, "build")
    return send_from_directory(build_dir, "index.html")

@survey.route('/seller_intake_survey_results')
@mongo
def seller_intake_survey_results(db):
    surveys = list(db['surveys'].find())
    return render_template("seller_intake_survey_results.html",surveys=surveys)