import pypyodbc

connection=connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=52.233.255.163;'
'Database=master;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=advancedProgramming2',autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE DATABASE Customer1;")
cursor.execute(SQLCommand)
print('done')

connection.close()

