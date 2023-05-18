from flask import Flask, render_template, jsonify, json, request, redirect
import requests
from convert import get_currency, convert

app = Flask(__name__)


url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()
keys = get_currency(data['rates'])

baseURL = 'https://api.exchangerate.host/'


@app.route('/')
def home():
    return render_template('index.html', currency=keys)


@app.route('/results', methods=['GET', 'POST'])
def results():
    value = request.args['value']
    from_value = request.args['from-value']
    to_value = request.args['to-value']
    response = convert(from_value, to_value, value)
    return render_template('result.html', response=response.json().get('result'), currency=to_value)
