# encoding: utf-8

import mysql.connector

from database.credentials import DB_HOST
from database.credentials import DB_SCHE
from database.credentials import DB_USER
from database.credentials import DB_PASS


SQL_CONNECTION = mysql.connector.connect(
	host=DB_HOST,
	database=DB_SCHE,
	user=DB_USER,
	passwd=DB_PASS,
	auth_plugin='mysql_native_password'
)



def basic_select(table_name, table_columns, table_conditions):

	query = open('database/queries/basic_select.sql')

	query_content = query.read()
	query_content = query_content.format(
		table_name=table_name,
		table_columns=table_columns,
		table_conditions=table_conditions
	)
	query.close()

	cursor = SQL_CONNECTION.cursor()
	cursor.execute(query_content)
	results = cursor.fetchall()
	cursor.close()

	return results
