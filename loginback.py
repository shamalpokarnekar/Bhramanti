#!C:\python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
pn=form.getvalue("pn")
#print(username)
password=form.getvalue("password")
#print(password)
mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="bhramanti")
mycursor=mydb.cursor()
query=f""" select * from registerform where phone_no='{pn}' AND password='{password}' """
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
#print(mycursor.rowcount)
if mycursor.rowcount==1:
    user_id=myresult[0]
    user_name=myresult[1]
    print(f'''
    <script>localStorage.clear();
    localStorage.setItem("id",'{user_id}');
    localStorage.setItem("name",'{user_name}');
    alert("Welcome user-{user_name}");
    </script>''')
    print(f'''
     <script>alert("Login Successfully...");
     location.href="index.py";
     </script>
     ''')
else:
     print(f'''
    <script>alert(" Login Unsuccessfully");
    location.href="loginform.py";
    </script>''')


