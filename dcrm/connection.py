import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '3122000'
)

cursorObjact = mydb.cursor()

cursorObjact.execute("CREATE DATABASE crmdb")

print('all is done!')