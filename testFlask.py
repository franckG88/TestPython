#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

@app.route('/albums')
def albums():
    return "Liste des Albums:"

if __name__ == '__main__':
    app.run(debug=True)
