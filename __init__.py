from flask import Flask
from survey.routes import survey

def create_app():
    app = Flask(__name__)
    app.register_blueprint(survey)
    return app
app = create_app()
app.run(debug=True, port="8000")
