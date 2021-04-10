#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, redirect, json
from flask import url_for, abort, session, jsonify
import sys
from urllib.parse import urlparse


app = Flask(__name__, template_folder='./templates/')



@app.route('/')
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response



if __name__ == '__main__':
    app.run()