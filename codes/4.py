import mysql.connector
try:
    mydbs = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="root",
        database = "student",
        port = 3308
    )
    if mydbs.is_connected():
        print("Connected successfullu")
except:
    print("Connection failed")

c = mydbs.cursor()
create_query = "CREATE TABLE EMPLOYEE2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), mobile VARCHAR(255), password VARCHAR(255))"
c.execute(create_query)
print("Table created successfully")

insert_query = "INSERT INTO EMPLOYEE2 (name, email, mobile, password) VALUES (%s, %s, %s, %s)"
values = [
    ("Ayush", "ayush@gmail.com", "9876543210", "ayush123"),
    ("Rohan", "rohan@gmail.com", "9876543211", "rohan123"),
    ("Ankit", "ankit@gmail.com", "9876543212", "ankit123"),
    ("Akshit", "akshitjainonly1@gamil.com", "9350558221", "akshit123")
]
c.executemany(insert_query, values)
print("Data inserted successfully")

mydbs.commit()