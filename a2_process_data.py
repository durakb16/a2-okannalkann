
import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]


i=0
j=0

print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset=\"utf-8\" />
<title> Fenerbahce Basket </title>
    <style>
        table, td 
		{
            border: 2px solid grey;
			color:#123123;
			font-weight:bold;
			width:40%;					
			height:50%; 
			background-color:#FFFFFF		
		}	
		h1
			{ 
			color: blue;
			font-size:1em;
			text-align:left;
			}
    </style>
</head>
<body>""")
print("<h1>Fenerbahçe Men Basketball Team</h1>")	
print("<table>")
for i in range(0,8):
	print("<tr>")
	for j in range(0,5):
		print("<td>"+str(contents[i][j]) + "</td>")
print("""</tr> 
</table>""")
print("""
</body>
</html>""")
