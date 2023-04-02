import mysql.connector


# mysql connection

con = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "rental_car")
# This is just a connection
cursor = con.cursor()
