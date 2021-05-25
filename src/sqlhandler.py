# -*- coding: utf-8 -*-
#!/usr/bin/python3

import mysql.connector as database
import importlib.machinery
loginCredentials = importlib.machinery.SourceFileLoader('login_credentials','conf/login_credentials.py').load_module()	# load sql login credentials from an external file
#import os

print('init sql handler')

sqlLoginUser = loginCredentials.loginData["user"]
sqlLoginPassword = loginCredentials.loginData["password"]
sqlLoginHost = loginCredentials.loginData["host"]

sqlSelectDatabase = "bookstore"

connection = database.connect(user = sqlLoginUser, password = sqlLoginPassword, host = sqlLoginHost, database = sqlSelectDatabase)
cursor = connection.cursor()

cursor.execute("SELECT * FROM books")
lst = cursor.fetchall()

print(lst)
