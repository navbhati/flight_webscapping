from os import name
from flask import Flask, render_template, request
from flight_data import getFlightData 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('web_design.html')


@app.route('/', methods=['POST'])
def formSubmit():
    print(request.form)
    return getFlightData(request.form).content


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)