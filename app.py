import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def mainpage():
	return "Hello from my python server"
	return "This is jenkins pipeline"

if(__name__=='__main__'):
	app.run(host='0.0.0.0',port=5000,debug=True)
