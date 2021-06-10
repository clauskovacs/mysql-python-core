# -*- coding: utf-8 -*-
#!/usr/bin/python3

import crawl
import sqlhandler

# crawling events testing
#driver_instance = crawl.crawler(True, 800, 600)
#driver = driver_instance.init_driver()
#driver_instance.fetch_page(driver)
#driver_instance.close_driver(driver)

# sql handler testing
sqlhandlerTest = sqlhandler.sqlhandler()

# fetch all existing DB
print('\nfetching all existing DB:')
returnAllDB = sqlhandlerTest.fetchAllDB(1)

print('\n')

selectDB = returnAllDB[0]['Database']
print ('fetching all tables for DB: ' + selectDB)
listStructureDB = sqlhandlerTest.fetchAllTablesfromDB(selectDB, 1)

print('\n')

sqlhandlerTest.fetchTableContent(selectDB, listStructureDB[0]['Tables_in_' + selectDB], 1)



print ('\nexiting')
