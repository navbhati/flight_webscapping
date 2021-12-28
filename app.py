from os import name
from flask import Flask, render_template, request,jsonify
from requests.models import Response
from werkzeug.wrappers import response
from flight_data import getFlightData 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('web_design.html')


@app.route('/', methods=['POST'])
def formSubmit():
    response = getFlightData(request.form)
    print(response)
    return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)