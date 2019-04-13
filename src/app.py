# -*- coding: utf-8 -*-

from database.extractor import basic_select
from database.extractor import agg_tags_stats

from encoders import MyJSONEncoder

from flask import Flask
from flask import jsonify
from flask import request

app = Flask('Facebook-backend')
app.json_encoder = MyJSONEncoder



@app.route('/get_data', methods=['GET', 'POST'])
def get_data():

	table_name = request.args.get('table_name')
	table_columns = request.args.get('table_columns')
	table_conditions = request.args.get('table_conditions')

	results = basic_select(table_name, table_columns, table_conditions)

	return jsonify(results)



@app.route('/get_tags_stats', methods=['GET', 'POST'])
def get_aggr_tags_stats():

	results = agg_tags_stats()
	return jsonify(results)



if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5000,
		debug=True
	)
