import serial
import os
import json
from os import system
import pymongo
import getpass
import hashlib
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGOLINK"))

mydb = client['BinData']
mycol = mydb["users"]

ser = serial.Serial('/dev/cu.usbmodem14101',baudrate = 9600)


print(ser.name)
x = 0
y = 0
itemno = 0
register = False
material = input("material: ")
user = input("user: ")

query = { "user": f"{user}" }
result = mycol.find_one(query)
truth = str(result["password"])
password = getpass.getpass('Password:').encode('utf-8')
hashresult = hashlib.sha256(password).hexdigest()

if truth == password:
	while 1:
		data = ser.readline().decode("ascii")
		print(data)

		if (x == 1) and ((float(data) < 7) and (float(data) > 5.75)):
			itemno = itemno + 1
			if register == True:
				if itemno > 1:
					system(f"say {str(itemno)} {material}s")
				else:
					system(f"say {str(itemno)} {material}")
				x = 0
				y = 0
				query = { "user": f"{search}" }
				result = mycol.find_one(query)
				newvalue = result["number"] + 1
				newvalues = { "$set": { "number": newvalue } }
				mycol.update_one(query, newvalues)
				for update in mycol.find():
			  		print(update) 
	
			else:
				system(f"say {material}")
		elif (float(data) > 7) or (float(data) < 5.75):
			print("poggers")
			y = y + 1
			x = 1
			if y == 100:
				itemno = 0
	ser.close()
else:
	system("python3 recieve.py")