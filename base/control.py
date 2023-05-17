import pymongo
from os import system
import getpass
import hashlib
import dns
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGOADMIN"))

mydb = client['BinData']
mycol = mydb["users"]
want = input("Request: ")

if want == "insert":
	user = input("new username: ")
	while True:
		email = input("email: ")
		password = str(getpass.getpass('Password:'))
		check = str(getpass.getpass('Retype Password:'))

		if password == check:
			password = password.encode('utf-8')
			hashresult = hashlib.sha256(password).hexdigest()
			newdict = { "user": f"{user}", "password": f"{hashresult}", "email": f"{email}", "number": 0 }
			add = mycol.insert_one(newdict)
			print(add)
			break
		else:
			print("\nPlease Try Again")
			continue

elif want == "viewall":	
	for thing in mycol.find():
	  print(thing) 

elif want == "view":
	search = input("username: ")
	query = { "user": f"{search}" }
	result = mycol.find(query)
	for found in result:
  		print(found) 

elif want == "add":
	search = input("username: ")
	query = { "user": f"{search}" }
	newvalue = input("value: ")
	newvalues = { "$set": { "number": newvalue } }
	mycol.update_one(query, newvalues)
	for update in mycol.find():
  		print(update) 

elif want == "delete":
	search = input("username: ")
	query = { "user": f"{search}" }
	recent = mycol.delete_one(query) 
	print(recent)

else:
	print("invalid function")
	system("python3 control.py")