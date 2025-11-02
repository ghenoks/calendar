from flask import Flask, request, jsonify
from flasgger import Swagger
import json
from models.calendar import Calendar
from exporters.exporter import CalendarExporter
from importers.importer import CalendarImporter
from transformers.dictionary_transformer import DictionaryTransformer
from controllers.calendar_controller import calendar_bp

# dictionary
# read ics file
# regex find words
# replace them with dictionary
# export it into ics file


###  look at what each class does
# divide the stuff into service layers and controllers, entities
# look into logic and how to improve

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(calendar_bp, url_prefix="/calendar")

@app.route("/")
def home():
    #TO DO
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)
