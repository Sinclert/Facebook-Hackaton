# encoding: utf-8

import mysql.connector

from database.credentials import DB_HOST
from database.credentials import DB_USER
from database.credentials import DB_PASS


SQL_CONNECTION = mysql.connector.connect(
	host=DB_HOST,
	user=DB_USER,
	passwd=DB_PASS,
)



def basic_select(table_name, table_columns, table_conditions):

	query = open('./queries/basic_select')

	query_content = query.read()
	query_content = query_content.format(
		table_name=table_name,
		table_columns=table_columns,
		table_conditions=table_conditions
	)
	query.close()

	cursor = SQL_CONNECTION.cursor()
	cursor.execute(query_content)
	cursor.close()

	return cursor.fetchall()
