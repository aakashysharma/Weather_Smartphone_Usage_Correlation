#Read database for data about video request
import yaml

with open("db.yaml",'r') as dbconfig:
    cfg = yaml.load(dbconfig)
#test config file read
print cfg['mysql']

import MySQLdb
#connect
db = MySQLdb.connect(host="localhost", user="lab", passwd="labuser", db="lab_usage_data")

cursor = db.cursor()

cursor.execute("select * from requests")

db.commit()

numrows = int(cursor.rowcount)

print numrows

db.close()
