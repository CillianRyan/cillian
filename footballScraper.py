import http.client, json, pypyodbc
#Set up a connection to the API
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

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

#Replace xxxxxxxxxxxxxxxxxxxxxxxx with API-Key.
with open(".apikey") as f:
  key = f.read()

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': key
    }
conn.request("GET", "/players/topscorers?season=2020&league=39", headers=headers)

#Variable that get the response from the api.
res = conn.getresponse()
#Read the data from the api
data = res.read()
#Convert the data to #json format.
info = json.loads(data)
#Print the data
#print(json.dumps(info, indent=4))

cur.execute('''DELETE FROM topScorers''')

counter = 0

while counter < len(info["response"]):
        for i in info["response"]:
                cur.execute('''INSERT INTO topScorers (firstName, lastName, age, nationality, team, appearances,  goals, assists)  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (info["response"][counter]["player"]["firstname"],
                info["response"][counter]["player"]["lastname"],
                info["response"][counter]["player"]["age"],
                info["response"][counter]["player"]["nationality"],
                info["response"][counter]["statistics"][0]["team"]["name"],
                info["response"][counter]["statistics"][0]["games"]["appearences"],
                info["response"][counter]["statistics"][0]["goals"]["total"],
                info["response"][counter]["statistics"][0]["goals"]["assists"]))
                conn2.commit()
                counter = counter + 1


with open(".apikey") as f:
  key = f.read()

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': key
    }
conn.request("GET", "/players/topassists?season=2020&league=39", headers=headers)

#Variable that get the response from the api.
res = conn.getresponse()
#Read the data from the api
data = res.read()
#Convert the data to #json format.
info = json.loads(data)
#Print the data
#print(json.dumps(info, indent=4))

cur.execute('''DELETE FROM topAssists''')

counter = 0

while counter < len(info["response"]):
        for i in info["response"]:
                cur.execute('''INSERT INTO topAssists (firstName, lastName, age, nationality, team, appearances,  goals, assists)  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (info["response"][counter]["player"]["firstname"],
                info["response"][counter]["player"]["lastname"],
                info["response"][counter]["player"]["age"],
                info["response"][counter]["player"]["nationality"],
                info["response"][counter]["statistics"][0]["team"]["name"],
                info["response"][counter]["statistics"][0]["games"]["appearences"],
                info["response"][counter]["statistics"][0]["goals"]["total"],
                info["response"][counter]["statistics"][0]["goals"]["assists"]))
                conn2.commit()
                counter = counter + 1


#Replace xxxxxxxxxxxxxxxxxxxxxxxx with API-Key.
with open(".apikey") as f:
  key = f.read()

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': key
    }
conn.request("GET", "/players/topyellowcards?season=2020&league=39", headers=headers)

#Variable that get the response from the api.
res = conn.getresponse()
#Read the data from the api
data = res.read()
#Convert the data to #json format.
info = json.loads(data)
#Print the data
#print(json.dumps(info, indent=4))

cur.execute('''DELETE FROM topYellows''')

counter = 0

while counter < len(info["response"]):
        for i in info["response"]:
                cur.execute('''INSERT INTO topYellows (firstName, lastName, age, nationality, team, appearances,  goals, assists, yellowCards, redCards)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (info["response"][counter]["player"]["firstname"],
                info["response"][counter]["player"]["lastname"],
                info["response"][counter]["player"]["age"],
                info["response"][counter]["player"]["nationality"],
                info["response"][counter]["statistics"][0]["team"]["name"],
                info["response"][counter]["statistics"][0]["games"]["appearences"],
                info["response"][counter]["statistics"][0]["goals"]["total"],
                info["response"][counter]["statistics"][0]["goals"]["assists"],
                info["response"][counter]["statistics"][0]["cards"]["yellow"],
                info["response"][counter]["statistics"][0]["cards"]["red"]))
                conn2.commit()
                counter = counter + 1



#Replace xxxxxxxxxxxxxxxxxxxxxxxx with API-Key.
with open(".apikey") as f:
  key = f.read()

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': key
    }
conn.request("GET", "/players/topredcards?season=2020&league=39", headers=headers)

#Variable that get the response from the api.
res = conn.getresponse()
#Read the data from the api
data = res.read()
#Convert the data to #json format.
info = json.loads(data)
#Print the data
#print(json.dumps(info, indent=4))

cur.execute('''DELETE FROM topReds''')

counter = 0

while counter < len(info["response"]):
        for i in info["response"]:
                cur.execute('''INSERT INTO topReds (firstName, lastName, age, nationality, team, appearances,  goals, assists, yellowCards, redCards)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (info["response"][counter]["player"]["firstname"],
                info["response"][counter]["player"]["lastname"],
                info["response"][counter]["player"]["age"],
                info["response"][counter]["player"]["nationality"],
                info["response"][counter]["statistics"][0]["team"]["name"],
                info["response"][counter]["statistics"][0]["games"]["appearences"],
                info["response"][counter]["statistics"][0]["goals"]["total"],
                info["response"][counter]["statistics"][0]["goals"]["assists"],
                info["response"][counter]["statistics"][0]["cards"]["yellow"],
                info["response"][counter]["statistics"][0]["cards"]["red"]))
                conn2.commit()
                counter = counter + 1

cur.close()

