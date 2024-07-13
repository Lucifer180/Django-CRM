import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shre.,rt018'
)


cursor_object = database.cursor()
cursor_object.execute("CREATE DATABASE shreyas3")
print('created')
