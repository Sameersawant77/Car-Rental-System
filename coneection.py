import mysql.connector
con = mysql.connector.connect(user = "root",
                            password = "",
                            host = "localhost",
                            database = "login_register")
# This is just a connection
cursor = con.cursor()
# To navigate through the table of database
query = cursor.execute("SELECT * FROM login_register_table")
r = cursor.fetchall()
print(r)
