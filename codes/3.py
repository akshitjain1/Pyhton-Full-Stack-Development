import mysql.connector
try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student",
        port = 3308
    )
    if con.is_connected():
        print("connected successfully")

except:
    print("connection failed")


# create_query = "CREATE TABLE data2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
c = con.cursor()
# c.execute(create_query)
# print("Table created successfully")

insert_query = "INSERT INTO data2 (name, age) VALUES (%s, %s)"
values = ("Ayush", 22)
c.execute(insert_query, values)
print("Data inserted successfully")

con.commit()