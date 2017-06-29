#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/albums')
def albums():
    return "Liste des Albums:"

@app.route('/artistes')
def albums():
    return "Liste des artistes:"

@app.route('/concerts')
def albums():
    return "Concerts à venir:"

if __name__ == '__main__':
    app.run(debug=True)
