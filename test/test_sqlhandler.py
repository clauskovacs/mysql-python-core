# -*- coding: utf-8 -*-
#!/usr/bin/python3

import unittest
from src import sqlhandler

class TestSum(unittest.TestCase):

	# test the function extractInsertInformation of the sqlhandler. This function
	# is part of the importfunction of a table to the DB. It parses a *.sql file
	# and extracts the desired information (which is to be inserted into the DB)
	def test_sqlhandler(self):
		file_sqltest_import = "test/sqlhandler_testtable_import.sql"

		# generate the to be expected result from the function
		expected_result = []
		column_headers = []

		testdata0 = ['', '', 'aaa', 0, 0, '', 2, '', '']
		expected_result.append(testdata0)
		col_header0 = ['varchar(100)', 'varchar(100)', 'varchar(100)', 'int(5)', 'int(5)',
						'varchar(300)', 'int(5)', 'varchar(5000)', 'varchar(150)']
		column_headers.append(col_header0)

		testdata1 = ['0805210407', 'The Trial', 1, None, '1992', 'None']
		expected_result.append(testdata1)
		col_header1 = ['char(20)', 'varchar(50)', 'int(11)', 'int(11)', 'char(4)', 'text']
		column_headers.append(col_header1)

		testdata2 = ['66.249.78.123', '2013-02-01 01:14:59']
		expected_result.append(testdata2)
		col_header2 = ['datetime', 'datetime']
		column_headers.append(col_header2)

		expected_result = tuple(map(tuple, expected_result))
		column_headers = tuple(map(tuple, column_headers))

		# read the file and perform the tests
		with open(file_sqltest_import, encoding='utf-8') as fp:
			line = fp.readline()

			i = 0

			while line:
				sqlhandler_Testobj = sqlhandler.SqlHandler()
				returnData = sqlhandler_Testobj.extractInsertInformation(line, column_headers[i])
				self.assertEqual(returnData, expected_result[i])
				line = fp.readline()
				i += 1

if __name__ == '__main__':
	unittest.main()
