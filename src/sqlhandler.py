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

		connection.close()

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

		connection.close()

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
		cursor.execute("SHOW COLUMNS FROM " + sqlSelectTable)
		fetchTableHeader = cursor.fetchall()

		if verbose == 1:
			for row in fetchTableHeader:
				print(f"{row[0]:>20} ", end = '')
			print('\n-----------------------------------------------------------------------------------')

		# fetch/print the table column data
		cursor.execute("SELECT * FROM " + sqlSelectTable)
		fetchTableContentData = cursor.fetchall()

		connection.close()

		# cout the table information
		if verbose == 1:
			for i in range(len(fetchTableContentData)):
				print(fetchTableContentData[i])
				#print(f"{str(fetchTableContentData[0][i]):>20} ", end = '')

		return fetchTableContentData, fetchTableHeader

	# Insert data into a Table
	def insertIntoTable(self, sqlSelectDatabase, insertStatement, insertData):
		connection = database.connect(user = self.sqlLoginUser, password = self.sqlLoginPassword, host = self.sqlLoginHost, database = sqlSelectDatabase)
		cursor = connection.cursor()
		cursor.execute(insertStatement, insertData)
		connection.commit()
		connection.close()

	# export a table (into a file on the disk). This file can for example be used in phpMyadmin to import the table
	def exportTable(self, path, createNewTable, exportDB, exportTable):
		# write the header to the file
		f = open(path, "w")
		f.write('SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";\n')
		f.write('START TRANSACTION;\n')
		f.write('SET time_zone = "+00:00";\n\n')

		if createNewTable == 1:
			f.write('CREATE TABLE `' + exportTable + '` (\n')

			# fetch the data
			tableData, tableHeaderData = self.fetchTableContent(exportDB, exportTable, 0)

			# create a list to be able to change the entries
			tableHeaderDataList = list(tableHeaderData)

			# replacements to make it compatible using, e.g., phpMyadmin
			replacements = {
				'PRI': 'PRIMARY KEY',
				'YES': '',
				#'None': '',
				'NO': 'NOT NULL'
			}

			# iterate over the list (create and write the data to the file)
			for i in tableHeaderDataList:
				# don't end the last line with a comma
				if i != tableHeaderDataList[-1]:
					endStr = ','
				else:
					endStr = ''

				# replace certain elements in the list
				i = [replacements.get(x, x) for x in i]

				# remove all elements containing 'None' (in the table header)
				res = [j for j in i if j]

				# create the string
				full_str = ' '.join([str(elem) for elem in res])
				f.write(full_str + endStr + "\n")

			f.write(") ENGINE=InnoDB DEFAULT CHARSET=latin1;\n\n")


			# create/write the data
			#
			# header:
			f.write('INSERT INTO `' + exportTable + '` ')

			tmpStr1 = "("

			for j in tableHeaderData:
				tmpStr1 += '`' + j[0] + '`, '

			# change the ending of the string
			tmpStr1 = tmpStr1[:-2] + ")"
			f.write(tmpStr1 + " VALUES \n")

			# data:
			for count, i in enumerate(tableData):
				tmpStr2 = "("

				for k in i:
					if type(k) == int:
						tmpStr2 += "" + str(k) + ", "
					else:
						tmpStr2 += "'" + str(k) + "', "

				# change the ending of the string
				tmpStr2 = tmpStr2[:-2] + ")"

				if count == len(tableData)-1:
					f.write(tmpStr2 + ";\n")
				else:
					f.write(tmpStr2 + ",\n")

			f.write("\nCOMMIT;")

		f.close()


