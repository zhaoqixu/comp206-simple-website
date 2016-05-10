#!/usr/bin/python
import cgi, cgitb

print "Content-type:text/html\r\n\r\n"

print "<html>"
print "<head>"
print "<title>Go to checkout</title>"
print "</head>"
print "<body bgcolor=\"tan\">"
print "<p style=\"margin-top: 30px;\">"
print "<h1 align=\"center\"><i>Bill</i></h1>"
print "</p>"
print "<p>"

form = cgi.FieldStorage() 

class obj:
	
	def __init__(self,x,n,p):
		self.name=x
		self.num=n
		self.price=p
def change(x):
	ob=[]	
	try:
		A=open("Inventory.csv","r")
		l=A.readlines()
		for i in l:
			i=i.split(",");
			if i[0]==x:
				i[1]=int(i[1])-1;
			ob.append(obj(i[0],i[1],i[2].strip()))
	except IOError:
		print "IOerror"
	A.close()
	A=open("Inventory.csv","w")
	for i in ob:
		tb=[i.name,i.num,i.price]
		v=",".join([i.name, str(i.num),i.price])
		A.write(v)
		A.write("\n")
	A.close()

def loggedin(username):
	try:
		name=open("LoggedIn.csv","r")
		for line in name.readlines():
			if line.strip() == username:
				return "1"
		return "0" 
		name.close()
	except IOError:
		print "Oops!LoggedIn.csv Missing"


# Get data from fields

username = form.getvalue('username')

mc = form.getvalue('mercury')
vn = form.getvalue('venus')
ms = form.getvalue('mars')
jp = form.getvalue('jupiter')
st = form.getvalue('saturn')

num1 = form.getvalue('num1')
num2 = form.getvalue('num2')	
num3 = form.getvalue('num3')
num4 = form.getvalue('num4')
num5 = form.getvalue('num5')


total = 0


list1 = [mc,vn,ms,jp,st];
list2 = ['Mercury','Venus','Mars','Jupiter','Saturn'];
list3 = [num1,num2,num3,num4,num5]

if loggedin(username) == "0":
	print "<p>You are not logged in.</p>"
	print "<a href=\"http://www.cs.mcgill.ca/~yxia18/store/catalogue.html\">CATALOGUE"
	print "</body> </html>"
else:
	quantity = open("Inventory.csv","r")

	
	
	
	for i in range(5):
		l=quantity.readline()
		l=l.split(",");
		
		if list1[i] == '0':
			
			
			if list3[i] > "1":
				print "<p>Sorry,We don't have so much stocks for %s</p>"%(list2[i])
			else:
				if list3[i] == "1":
					if l[1] < "1":
						print "<br><center>%s Sold Out<center>"%(list2[i])
					else:
						if l[1] == "1":
							
							print "<p><center>Iterm name:%s</center></p>"%(list2[i])
							print "<p><center>Iterm quantity:%s</center></p>"%(list3[i])
							print "<p><center>Iterm price:%s</center></p>"%(l[2])
							change(list2[i])
							total = total + int(l[2])
		
	quantity.close()
	
	print "<p><center>The total amount is %d.</center></p>"%(total)
	print "<p style=\"line-height: 80px;\">"
	print "<a href=\"http://www.cs.mcgill.ca/~yxia18/store/home.html\">HOME</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<a href=\"http://www.cs.mcgill.ca/~yxia18/store/catalogue.html\">CATALOGUE</a>"
	print "</p>"
	print "</body></html>"
	






	


