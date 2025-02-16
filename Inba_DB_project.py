import mysql.connector as mysql
db = mysql.connect(host="localhost",
            user="root",password="Snekha@2503")

cursor=db.cursor()
# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS StudentDBone")

cursor.execute("USE StudentDBone")

cursor.execute("CREATE TABLE IF NOT EXISTS Students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),age INT,grade varchar(3))")

name="Inba"
age=17
grade="A"
cursor.execute("INSERT INTO Students(name,age,grade) values (%s,%s,%s)",(name,age,grade))
cursor.execute("INSERT INTO Students(age,name,grade) values (20,'Ram','A')")
db.commit()#save the data

