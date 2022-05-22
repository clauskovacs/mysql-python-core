![](https://github.com/clauskovacs/mysql-python-core/workflows/mysql-python-core/badge.svg)

# mysql-python-core
Building upon *mysql-python-connect-test* (https://github.com/clauskovacs/mysql-python-connect-test), this program implements some basic routines to interact with a database.

## Description
Utilizing the class **SqlHandler**, following database operations are provided:
1. **fetch_all_db(...)** *(Retrieve / list all existing databases)*
2. **fetch_all_tables(...)** *(Retrieve all tables from a given DB on the SQL server)*
3. **fetch_table_content(...)** *(Fetch data from a given table for a selected database and table)*
4. **insert_into_table(...)** *(Insert data into a table of a database.)*
5. **create_table(...)** *(Create a new table)*
6. **drop_table(...)** *(Delete a table from a selected database)*
7. **truncate_table(...)** *(Clear (truncate) a table)*
8. **export_table(...)** *(Export a table from the SQL server to a (local) file on the disk)*
9. **import_table(...)** *(Import a (local) file into the SQL server)*

Some of the functions are used in https://github.com/higgsAT/lecture-free-time-extract.

## Folder Structure
This project has the following folder structure
```
.
├── logs
├── src
    ├── config_example.py
    └── sqlhandler.py
└── test
    ├── sqlhandler_testtable_import.sql
    └── test_sqlhandler.py
```
The folder */src* contains the SqlHandler-class and additionally the config file for the login credentials. The folder */test* contains the CI unit tests.

## Dependencies / Installation
See https://github.com/clauskovacs/mysql-python-connect-test

## Running the Program
Import the file:
`import sqlhandler`

Create/Initialise a class object initialisation:
`sqlhandlerObj = sqlhandler.SqlHandler()`

Invoke a database function, e.g.,:
`getTableData = sqlhandlerObj.fetch_table_content(...)`

## Additionall Information
This class and (some of its) functions have been used in:
1. https://github.com/higgsAT/lecture-free-time-extract
