# -*- coding: utf-8 -*-
#!/usr/bin/python3

import unittest
from src import sqlhandler

class TestSum(unittest.TestCase):

	#def test_sum(self):
		#self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

	#def test_sum_tuple(self):
		#self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

	def test_sqlhandler(self):
		filename = "test/sqlhandler_testtable_import.sql"

		t = []	# expected extracted results
		z = []


		t0 = ['', '', 'aaa', 0, 0, '', 2, '', '']
		#toAllStr = [str(i) for i in t0]
		#t.append(toAllStr)
		t.append(t0)
		z0 = ['varchar(100)', 'varchar(100)', 'varchar(100)', 'int(5)', 'int(5)', 'varchar(300)', 'int(5)', 'varchar(5000)', 'varchar(150)']
		z.append(z0)

		t1 = ['0805210407', 'The Trial', 1, None, '1992', 'None']
		#t1AllStr = [str(i) for i in t1]
		#t.append(t1AllStr)
		t.append(t1)
		z1 = ['char(20)', 'varchar(50)', 'int(11)', 'int(11)', 'char(4)', 'text']
		z.append(z1)


		t2 = ['66.249.78.123', '2013-02-01 01:14:59']
		t.append(t2)
		z2 = ['datetime', 'datetime']
		z.append(z2)

		#tt = tuple(t)
		tt = tuple(map(tuple, t))
		zz = tuple(map(tuple, z))

		#print("\n\n", tt)
		#print(zz, "\n\n")

		#print("\n\n")
		#print(tt[1])
		#print("\n\n")

		#exit()

		i = 0

		with open(filename, encoding='utf-8') as fp:
			line = fp.readline()
			#print(line)

			while line:
				#print("{}".format(line.strip()))

				#print("LINE: ", line)

				sqlhandlerTest = sqlhandler.sqlhandler()

				returnData = sqlhandlerTest.extractInsertInformation(line, z[i])

				#print(returnData, "returnData: ", type(returnData))
				#print(tt[i], "tt[i]: ", type(tt[i]))

				"""
				print("COMPARE:")
				print(tt[i])
				print(returnData)
				"""

				self.assertEqual(returnData, tt[i])

				line = fp.readline()
				i += 1

		self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")



if __name__ == '__main__':
	unittest.main()


