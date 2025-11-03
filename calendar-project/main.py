from flask import Flask, request, jsonify
from flasgger import Swagger
from controllers.calendar_controller import calendar_bp

# TODO - fix why it adds extra day to end
# TODO - add dict for different languages and language choice option

# TODO - add other transformers
# TODO - embedding method

# TODO - add user defined mapping
# TODO - different languages

# TODO - frontend website
# TODO - add box for users to try sentence -> emoji before actual transformation

# TODO - return .ics to be downloadable

# TODO - docker

# TODO - GraphAPI integration

# TODO - user accounts?
# TODO - database for calendars and users?
# TODO - database for custom mappings

# TODO - logs


app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(calendar_bp, url_prefix="/calendar")

@app.route("/")
def home():
    # TODO
    return "Welcome to Calendar Transformer!"

if __name__ == "__main__":
    app.run(debug=True)
