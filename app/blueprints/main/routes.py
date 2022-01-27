from flask import render_template, request
import requests
from .import bp as main

@main.route('/', methods = ['GET'])

def index():
    return render_template('index.html')