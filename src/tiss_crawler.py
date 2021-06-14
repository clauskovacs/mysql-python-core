# -*- coding: utf-8 -*-
#!/usr/bin/python3

import crawl
import sqlhandler

# crawling events testing
#driver_instance = crawl.crawler(True, 800, 600)
#driver = driver_instance.init_driver()
#driver_instance.fetch_page(driver)
#driver_instance.close_driver(driver)

## sql handler testing ##
sqlhandler_testobj = sqlhandler.SqlHandler()


## fetch all existing DB ##
print('\nfetching all existing DB:')
returnAllDB = sqlhandler_testobj.fetch_all_db(1)

print('\n')

## fetch all tables from a DB ##
selectDB = returnAllDB[0]['Database']
print ('fetching all tables for DB: ' + selectDB)
listStructureDB = sqlhandler_testobj.fetch_all_tables(selectDB, 1)

print('\n')

selectTable = listStructureDB[0]['Tables_in_' + selectDB]
print("select table: ", selectTable)
sqlhandler_testobj.fetch_table_content(selectDB, selectTable, 1)

print('\n')


## INSERT TEST ##
selectTable = "2013__2013_02_28_23_55_21"

insertStatement = (
	"INSERT INTO " + selectTable +" (IP, Date) "
	"VALUES (%s, %s)"
)
insertData = ('168.172.0.0', '2000-0-0 00:00:00')

sqlhandler_testobj.insert_into_table(selectDB, insertStatement, insertData, 0)




## EXPORT TABLE TEST ##
path = "sql_IO/"
filename = "sql_export_test.sql"
appendOnly = 0	# export with CREATE TABLE
sqlhandler_testobj.export_table(path+filename, appendOnly, "bookstore", "2013__2013_02_28_23_55_21")



## CREATE TABLE TEST ##
columnInfo = "name VARCHAR(255), address VARCHAR(255)"
tableName = "customers"
sqlhandler_testobj.create_table("bookstore", tableName, columnInfo)


## DELETE TABLE TEST ##
sqlhandler_testobj.drop_table("bookstore", "customers")



## TRUNCATE TABLE TEST ##
sqlhandler_testobj.truncate_table("bookstore", "books")


## IMPORT TABLE TEST ##
path = "sql_IO/"
filename = "import_test.sql"
sqlhandler_testobj.import_table(path+filename, "bookstore")


print ('\nexiting')
