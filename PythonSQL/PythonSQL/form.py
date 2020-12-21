import cgi
from PythonSQL import getconnection, addCity, printtable

form = cgi.FieldStorage()
city = form.getfirst("Город", "не задан")
connection = getconnection()

(connection.cursor(), cities)
connection.commit()

print("Content-type: text/html\n")
print(f"""
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>{printtable(connection.cursor(), "cities")}</h1>
</body>
</html>""")

