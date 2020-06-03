import os
import time
import pandas as pd
import hashlib as hash
from getpass import getpass

users = None
username = None
messageFile = 'Chats/{}/{}'
usersFile = 'Chats/users.csv'

try:
	os.makedirs("Chats")
except FileExistsError:
	pass

try:
	csv_old = pd.read_csv(usersFile) # read the old csv file
except:
	oldCsvExists = False
else:
	oldCsvExists = True

def Login():
	global users
	global username
	if not oldCsvExists:
		print("No users found in database, create a new one!")
		CreateLogin()

	print("Autenticate yourself...")
	username = input("Please enter your username\n ").strip()
	password = getpass("Please enter your password\n ").strip().encode('utf-8')
	password = hash.sha1(password).hexdigest()

	users=[csv_old['username'][i] for i in range(len(csv_old))]
	passwords=[csv_old['password'][i] for i in range(len(csv_old))]

	userExists = False

	if username in users:
		for i in range(len(users)):
			if username == users[i] and password == passwords[i]:
				userExists = True
		if userExists:
			Home()
		else:
			print("Password does not match\n")
	else:
		choice = input("Username not found, you want to create a new one? (y/n) ").strip()
		if choice == 'y' or choice == 'Y':
			CreateLogin()
		else:
			Login()

def CreateLogin():
	global csv_old
	global username
	
	username = input("Please enter the new username\n ").strip() # required username field
	password = getpass("Please enter a password\n ").strip().encode('utf-8') # required password field
	password = hash.sha1(password).hexdigest() # password hashing
	
	csv = pd.DataFrame({'username': [username], 'password': [password]}) # create a new csv variable

	nameAlreadyUsed = (username in [csv_old['username'][i] for i in range(len(csv_old))] if oldCsvExists else False)
	
	csv_old = (pd.concat([csv_old, csv]) if oldCsvExists and not nameAlreadyUsed else csv) # if an old csv file exists concatenate it with the new one
	
	if nameAlreadyUsed:
		print("Username already in use, choose another username")
		CreateLogin()
	else:
		os.makedirs(messageFile.format(username, "")) # create a folder for the new user

	csv_old.to_csv(usersFile, index=False, encoding='utf-8') # csv file is created/written
	Login()

def WriteFile(file, data):
	file = open(file, 'a')
	file.write(data)
	file.close()

def Home():
	while True:
		chats = [file for file in os.listdir(messageFile.format(username,''))] # Legge tutte le chat dell'utente 

		for i in range(len(chats)):
			print("{}) {}".format(i, chats[i]))

		choice = input("\nYou want to [C]reate a new chat or [J]oin a previous one: ").strip()

		chatName = input("\nEnter chat name: ").strip()
		
		chatFile = messageFile.format(username, chatName)
		
		if choice != "":
			print("Write 'exit;' to exit a chat")
			if choice == 'J' or choice == 'j':
				if chatName in chats:
					print(open(chatFile, 'r').read()) # stampa tutti i messaggi della chat selezionata
				else:
					print("Chat not found")
			elif choice == 'C' or choice == 'c':
				if chatName in users:
					try:
						importedChat = messageFile.format(chatName, username)
						print(open(importedChat, 'r').read())
					except FileNotFoundError:
						file = open(chatFile, 'a')
						file.close()
					else:
						chatFile = importedChat
		else:
			print("Choice error")
			break

		Message(chatFile)

def Message(chatFile):
	while True:
		ora = "[{}/{}/{}] {}:{}:{}".format(time.localtime()[2],time.localtime()[1],time.localtime()[0],time.localtime()[3],time.localtime()[4],time.localtime()[5])
		
		message = input(" ")

		if message == "exit;":
			print("")
			break
		else:
			message = "{} [{}]: {}\n".format(ora, username, message)
			WriteFile(chatFile, message)

Login()

