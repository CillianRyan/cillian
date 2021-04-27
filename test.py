import pypyodbc
with open(".pw") as f:
  password = f.read()

connection=connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=cilliandb.dbsprojects.ie;'
'Database=master;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD='+password,autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE DATABASE Customer2;")
cursor.execute(SQLCommand)
print('done')

connection.close()

