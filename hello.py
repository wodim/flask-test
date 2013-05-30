# -*- coding: utf-8 -*-
from flask import *
app = Flask(__name__)

@app.after_request
def after_request(response):
	response.headers.remove('Server')
	response.headers.add('Server', 'fried')
	return response

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('hello.html', name = request.form['name'])
	else:
		return render_template('name.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 8080)
