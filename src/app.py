# -*- coding: utf-8 -*-

from database.extractor import basic_select

from flask import Flask
from flask import jsonify
from flask import request

app = Flask('Facebook-backend')



@app.route('/getdata', methods=['GET', 'POST'])
def get_data():

	table_name = request.args.get('table_name')
	table_columns = request.args.get('table_columns')
	table_conditions = request.args.get('table_conditions')
	print(table_name)
	print(table_columns)
	print(table_conditions)

	results = basic_select(table_name, table_columns, table_conditions)

	return jsonify(results)



if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5000,
		debug=True
	)
