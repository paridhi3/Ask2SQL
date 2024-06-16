import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create cursor to create, insert, retrieve, 
cursor = connection.cursor()

# Create table
table_info="""
Create table STUDENT(ID INT, NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

# Insert records

cursor.execute('''Insert Into STUDENT values(1001, 'Paridhi','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values(1002, 'Rishabh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values(1003, 'Swastika','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values(1004, 'Aaryan','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values(1005, 'Rahul','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values(1006, 'Sanya','Data Science','B',92)''')
cursor.execute('''Insert Into STUDENT values(1007, 'Aman','DEVOPS','B',65)''')
cursor.execute('''Insert Into STUDENT values(1008, 'Vikram','Data Science','A',78)''')
cursor.execute('''Insert Into STUDENT values(1009, 'Ishita','AI','A',88)''')
cursor.execute('''Insert Into STUDENT values(1010, 'Raj','AI','B',72)''')
cursor.execute('''Insert Into STUDENT values(1011, 'Ananya','Cyber Security','A',95)''')
cursor.execute('''Insert Into STUDENT values(1012, 'Kabir','Cyber Security','B',68)''')
cursor.execute('''Insert Into STUDENT values(1013, 'Priya','Data Science','A',89)''')
cursor.execute('''Insert Into STUDENT values(1014, 'Nisha','DEVOPS','B',55)''')
cursor.execute('''Insert Into STUDENT values(1015, 'Tara','AI','A',91)''')
cursor.execute('''Insert Into STUDENT values(1016, 'Varun','Cyber Security','A',73)''')

# Dispaly all records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the databse
connection.commit()
connection.close()