import flask
from flask import request, jsonify
from covid_parser import parsePage

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/cases/all', methods=['GET'])
def api_all():
    return jsonify(parsePage())

if __name__ == "__main__":
    app.run()
