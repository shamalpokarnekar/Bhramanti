#!C:\python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
name=form.getvalue("name")
#print(name)
pn=form.getvalue("pn")
#print(pn)
email=form.getvalue("email")
#print(email)
password=form.getvalue("password")
#print(password)
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bhramanti")
mycursor=mydb.cursor(dictionary=True)
query=f""" INSERT INTO `registerform`( `name`, `phone_no`, `email`, `password`) VALUES ('{name}','{pn}','{email}','{password}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
     <script>alert("Register Successfully...");
     location.href="register.py";
     </script>
''')