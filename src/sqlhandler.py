# -*- coding: utf-8 -*-
#!/usr/bin/python3

import mysql.connector as database
import importlib.machinery
loginCredentials = importlib.machinery.SourceFileLoader('login_credentials','conf/login_credentials.py').load_module()	# load sql login credentials from an external file

class sqlhandler:
	def __init__(self):
		print ('creating sqlhandler class object (init)\n')

		# set the login credentials
		self.sqlLoginUser = loginCredentials.loginData["user"]
		self.sqlLoginPassword = loginCredentials.loginData["password"]
		self.sqlLoginHost = loginCredentials.loginData["host"]

	# retrieve / list all existing databases
	def fetchAllDB(self, verbose):
		connection = database.connect(user = self.sqlLoginUser, password = self.sqlLoginPassword, host = self.sqlLoginHost)
		cursor = connection.cursor(dictionary = True)

		cursor.execute("SHOW DATABASES")
		queryAllDB = cursor.fetchall()

		# cout all found databases
		if verbose == 1:
			for row in queryAllDB:
				print (row['Database'])

		return queryAllDB

	# retrieve the tables from a DB
	def fetchAllTablesfromDB(self, sqlSelectDatabase, verbose):
		connection = database.connect(user = self.sqlLoginUser, password = self.sqlLoginPassword, host = self.sqlLoginHost, database = sqlSelectDatabase)
		cursor = connection.cursor(dictionary = True)

		cursor.execute("SHOW TABLES")
		queryAllTables = cursor.fetchall()

		# cout the information
		if verbose == 1:
			for row in queryAllTables:
				print (row['Tables_in_' + sqlSelectDatabase])

		return queryAllTables

	# fetch data from a given table
	def fetchTableContent(self, sqlSelectDatabase, sqlSelectTable, verbose):
		connection = database.connect(user = self.sqlLoginUser, password = self.sqlLoginPassword, host = self.sqlLoginHost, database = sqlSelectDatabase)
		cursor = connection.cursor()

		# fetch/print the header (table column names)
		if verbose == 1:
			cursor.execute("SHOW COLUMNS FROM " + sqlSelectTable)
			fetchTableHeader = cursor.fetchall()
			for row in fetchTableHeader:
				print(f"{row[0]:>20} ", end = '')
			print('\n-----------------------------------------------------------------------------------')

		# fetch/print the table column data
		cursor.execute("SELECT * FROM " + sqlSelectTable)
		fetchTableContent = cursor.fetchall()

		# cout the table information
		if verbose == 1:
			for i in range(len(fetchTableContent[0])):
				print(f"{str(fetchTableContent[0][i]):>20} ", end = '')
