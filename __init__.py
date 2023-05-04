from flask import Flask
from survey.routes import survey

app = Flask(__name__)
app.register_blueprint(survey)

app.run(debug=True, port="8000")
