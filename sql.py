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
cursor.execute('''Insert Into STUDENT values('Sanya','Data Science','B',92)''')
cursor.execute('''Insert Into STUDENT values('Aman','DEVOPS','B',65)''')
cursor.execute('''Insert Into STUDENT values('Vikram','Data Science','A',78)''')
cursor.execute('''Insert Into STUDENT values('Ishita','AI','A',88)''')
cursor.execute('''Insert Into STUDENT values('Raj','AI','B',72)''')
cursor.execute('''Insert Into STUDENT values('Ananya','Cyber Security','A',95)''')
cursor.execute('''Insert Into STUDENT values('Kabir','Cyber Security','B',68)''')
cursor.execute('''Insert Into STUDENT values('Priya','Data Science','A',89)''')
cursor.execute('''Insert Into STUDENT values('Nisha','DEVOPS','B',55)''')
cursor.execute('''Insert Into STUDENT values('Tara','AI','A',91)''')
cursor.execute('''Insert Into STUDENT values('Varun','Cyber Security','A',73)''')

# Dispaly all records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the databse
connection.commit()
connection.close()