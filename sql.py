import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create cursor to create, insert, retrieve, 
cursor = connection.cursor()

# Create table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

# Insert records

cursor.execute('''Insert Into STUDENT values('Paridhi','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rishabh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Swastika','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Aaryan','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Rahul','DEVOPS','A',35)''')

# Dispaly all records
print("The isnerted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes int the databse
connection.commit()
connection.close()