# -*- coding: utf-8 -*-
#!/usr/bin/python3

import mysql.connector as database
import importlib.machinery
loginCredentials = importlib.machinery.SourceFileLoader('login_credentials','conf/login_credentials.py').load_module()	# load sql login credentials from an external file

class sqlhandler:
	def __init__(self):
		print ('creating sqlhandler class object')

		# set the login credentials
		self.sqlLoginUser = loginCredentials.loginData["user"]
		self.sqlLoginPassword = loginCredentials.loginData["password"]
		self.sqlLoginHost = loginCredentials.loginData["host"]

	def testfetchDB(self, sqlSelectDatabase):
		connection = database.connect(user = self.sqlLoginUser, password = self.sqlLoginPassword, host = self.sqlLoginHost, database = sqlSelectDatabase)
		cursor = connection.cursor()

		cursor.execute("SELECT * FROM books")
		lst = cursor.fetchall()

		print(lst)
