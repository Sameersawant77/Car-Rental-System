import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login_register"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM login_register_table WHERE user_name = %s"
adr = ("admin",)

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
