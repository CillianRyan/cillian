from flask import Flask
from flask import request
from flask_cors import CORS
import json
import pypyodbc
app = Flask(__name__)
CORS(app)

with open(".pw") as f:
  password = f.read()

conn2 = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=cilliandb.dbsprojects.ie;'
'Database=Footballdb;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD='+password,autocommit = True)

cur = conn2.cursor()


@app.route("/topScorers")
def topScorers():
  cur = conn2.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM topScorers''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['firstName']=row[0].replace('\n',' ')
    Result['lastName']=row[1]
    Result['age']=row[2]
    Result['nationality']=row[3]
    Result['team']=row[4]
    Result['appearances']=row[5]
    Result['goals']=row[6]
    Result['assists']=row[7]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
  
@app.route("/topAssists")
def topAssists():
  cur = conn2.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM topAssists''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['firstName']=row[0].replace('\n',' ')
    Result['lastName']=row[1]
    Result['age']=row[2]
    Result['nationality']=row[3]
    Result['team']=row[4]
    Result['appearances']=row[5]
    Result['goals']=row[6]
    Result['assists']=row[7]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
