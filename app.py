from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
with open('.mysql_config') as f:
  mysql_config=json.loads(f.read())
app.config['MYSQL_USER'] = mysql_config['user']
app.config['MYSQL_PASSWORD'] = mysql_config['pass']
app.config['MYSQL_DB'] = mysql_config['db']
app.config['MYSQL_HOST'] = mysql_config['host'] #for now
mysql.init_app(app)

@app.route("/add") #Add Student
def add():
  name = request.args.get('name')
  email = request.args.get('email')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''INSERT INTO students(studentName, email) VALUES('{}','{}');'''.format(name,email)
  cur.execute(s)
  mysql.connection.commit()

  return '{"Result":"Success"}'

@app.route("/delete") #Delete Student
def delete():
 id2 = request.args.get('id')
 cur = mysql.connection.cursor()
 s = "delete from students where studentID = '%s'" % id2
 cur.execute(s)
 mysql.connection.commit()

 return '{"Result":"Delete Successful"}'
 
@app.route("/update") #Update Student
def update():
 id2 = request.args.get('id')
 name = request.args.get('name')
 email = request.args.get('email')
 #print (id2)
 #print (name)
 #print (email)
 cur = mysql.connection.cursor()
 s = '''UPDATE students SET studentName = '%s', email = '%s' WHERE studentID = %s''' %(name,email,id2)
 #print (s)
 cur.execute(s)
 mysql.connection.commit()
 
 return '{"Result":"Successfully Updated"}'

#@app.route("/delete") #Add Student
#def delete2():
 #return '{"Result":"Not Yet Implemented"}'
  
#@app.route("/deleted") #Add Student
#def deleted():
 #return '{"Result":"Not Yet done"}'

@app.route("/") #Default - Show Data
def hello(): # Name of the method
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM students''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['Name']=row[0].replace('\n',' ')
    Result['Email']=row[1]
    Result['ID']=row[2]
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
