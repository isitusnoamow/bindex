import serial
import os
import json
from os import system
import pymongo
import getpass
import hashlib
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGOLINK"))

mydb = client['BinData']
mycol = mydb["users"]

ser = serial.Serial('/dev/cu.usbmodem14101',baudrate = 9600)


print(ser.name)
x = 0
y = 0
z = 0
itemno = 0
register = True
#material = input("material: ")
user = input("user: ")

query = { "user": f"{user}" }
result = mycol.find_one(query)
#truth = str(result["password"])
#password = getpass.getpass('Password:').encode('utf-8')
#hashresult = hashlib.sha256(password).hexdigest()

#if truth == hashresult:
if 1 == 1:
	while 1:
		data = ser.readline().decode("ascii")
		print(data)

		if (x == 1) and ((float(data) < 26) or (float(data) > 36)):
			itemno = itemno + 1
			if register == True:
				if itemno > 1:
					#print(f"{str(itemno)} {material}s")
					print(f"{str(itemno)} thingy")
				else:
					#print(f"{str(itemno)} {material}")
					print(f"{str(itemno)} thingys")
				x = 0
				y = 0
				query = { "user": f"{user}" }
				result = mycol.find_one(query)
				newvalue = result["number"] + 1
				newvalues = { "$set": { "number": newvalue } }
				f = open('base.html','w')
				f.write(f"""<!DOCTYPE html>
<html>
<head>
	 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
	 <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	 <link rel="stylesheet" href="base.css">
	 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
	 <meta charset="UTF-8">
	<title>Profile</title>
</head>
<body>

	<!-- navbar -->

	<nav class="navbar navbar-expand-lg navbar-darl bg-dark">
	  <div class="container-fluid">
		<a class="navbar-brand" href="#">
			<img src="https://cdn.discordapp.com/attachments/760369737284452372/792587214147026954/bindex.png" width="50px" height="50px">
		</a>
		<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		  <span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarNav">
		  <ul class="navbar-nav">
			<li class="nav-item">
			  <a class="nav-link active" aria-current="page" href="#">Profile</a>
			</li>
			<li class="nav-item">
			  <a class="nav-link" href="#">Your Bins</a>
			</li>
			<li class="nav-item">
			  <a class="nav-link" href="#">BinMap</a>
			</li>
			<li class="nav-item">
			  <a class="nav-link disabled" href="#">Shop</a>
			</li>

		  </ul>
		  <ul id="so" class="navbar-nav px-3">
			<li id="name">
				<a class="nav-link"href="#">Admin</a>
			</li>
			<li id="profiel">
				<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
				  <path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 0 0 8 15a6.987 6.987 0 0 0 5.468-2.63z"/>
				  <path fill-rule="evenodd" d="M8 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
				  <path fill-rule="evenodd" d="M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z"/>
				</svg>
			</li>
			<li class="nav-item text-nowrap">
			  <a class="nav-link" href="#">Sign out</a>
			</li>
		</ul>
		</div>
	  </div>
	</nav>

	<div id="random" class="container marketing">
		<div class="row">
		  <div class="col-lg-4">
			<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
			  <path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 0 0 8 15a6.987 6.987 0 0 0 5.468-2.63z"/>
			  <path fill-rule="evenodd" d="M8 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
			  <path fill-rule="evenodd" d="M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z"/>
			</svg>

			<h2>Admin</h2>
			<p id="and">Joined at: 9/12/2020 <br>
			Badges: 1/20 <br>
			Bins setup: 1</p>
		  </div><!-- /.col-lg-4 -->
		  <div class="col-lg-4">
			<h2 id="title1">Points:</h2>
			<p id="current">{newvalue}</p>
		  </div><!-- /.col-lg-4 -->
		  <div class="col-lg-4">
			<h2 id="stats">Stats</h2>
			<p id="total">Total Points gained: {newvalue}</p>
			<p id="plastic">Total Plastic Recycled: {newvalue}</p>
			<p id="metal">Total Metal Recycled: 0</p>
			<p id="paper">Total Paper Mass Recycled: 0</p>
		  </div><!-- /.col-lg-4 -->
		</div>
	</div>

	<div id="badges">
		<div id="badgetitle">
			<h1>Badges:</h1>
		</div>
		<ul>
			<li>
				<img id="border" src="https://cdn.discordapp.com/attachments/760369737284452372/792655889189437440/Untitled_Artwork_2.png" width="200" height="200">
			</li>
			<li>
				<img id="border2" src="https://cdn.discordapp.com/attachments/774534377031598081/793042314058006528/Untitled_Artwork_8.png" width="200" height="200">
			</li>
		</ul>
	</div>
	

</body>
</html>""")
				mycol.update_one(query, newvalues)
				for update in mycol.find():
					print(update) 

	
			else:
				#print(f"{material}")
				print(f"thingy")
				#system(f"say {material}")
		elif (float(data) < 26) or (float(data) > 38):
			z = z + 1
			print(z)
			if z == 100:
				print("sending mail")
				context = ssl.create_default_context()
				with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
					server.login(os.getenv("EMAIL"), os.getenv("EMAILPASSWORD"))
					server.sendmail(os.getenv("EMAIL"), result["email"], "Your bin is full")
				exit()
		elif (float(data) > 26):
			print("nothing")
			y = y + 1
			x = 1
			z = 0
	ser.close()
else:
	print("wrong passowrd")
	system("python3 recieve.py")