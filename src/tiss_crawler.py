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
sqlhandlerTest = sqlhandler.sqlhandler()

## fetch all existing DB ##
print('\nfetching all existing DB:')
returnAllDB = sqlhandlerTest.fetchAllDB(1)

print('\n')

## fetch all tables from a DB ##
selectDB = returnAllDB[0]['Database']
print ('fetching all tables for DB: ' + selectDB)
listStructureDB = sqlhandlerTest.fetchAllTablesfromDB(selectDB, 1)

print('\n')

selectTable = listStructureDB[0]['Tables_in_' + selectDB]
sqlhandlerTest.fetchTableContent(selectDB, selectTable, 1)

print('\n')

## INSERT TEST ##
"""
insertStatement = (
	"INSERT INTO " + selectTable +" (name_last, name_first, country) "
	"VALUES (%s, %s, %s)"
)
insertData = ('Jane', 'Doe', 'muh')

sqlhandlerTest.insertIntoTable(selectDB, insertStatement, insertData)
"""

## EXPORT TABLE TEST ##
path = "sql_IO/"
filename = "sql_export_test.sql"
createNewTable = 1
sqlhandlerTest.exportTable(path+filename, createNewTable, "bookstore", "books")

print ('\nexiting')
