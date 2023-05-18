from flask import Flask, render_template, jsonify, json, request, redirect
import requests

baseURL = 'https://api.exchangerate.host/'


def get_currency(dict):
    for key in dict:
        return [key for key in dict.keys()]


def convert(from_value, to_value, amount):
    res = requests.get(f'{baseURL}/convert', params={'from': from_value,
                                                     'to': to_value, 'amount': amount})
    return res
