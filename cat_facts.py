import time
import os
import random
import Contact
import json
import smtplib
import string

#create providers
CONTACTS_FILE = "contacts.json"
FACTS_FILE = "facts.txt"


providers = { 'boost' : '@myboostmobile.com',
			  'tmobile' : '@tmomail.net',
			  'virgin' : '@vmobl.com',
			  'cingular' : '@cingularme.com',
			  'sprint' : '@messaging.sprintpcs.com',
			  'verizon'  : '@vtext.com',
			  'nextel' : '@messaging.nextel.com',
			  'cellular' : '@email.uscc.net',
			  'suncom' : '@tms.suncom.com',
			  'powertel' : '@ptel.net',
			  'att' : '@txt.att.net',
			  'alltell' : '@message.alltel.com',
			  'metropcs' : '@MyMetroPcs.com' }


def parseContacts(fileName):
	allContacts = []

	jsonFile = open(fileName)
	data = json.load(jsonFile)

	for i in range(len(data)):
		name = data[i]["name"]
		number = data[i]["number"]
		provider = data[i]["provider"]

		numMail = number + providers[provider]

		c = Contact.Contact(name, number, provider, numMail)

		allContacts.append(c)

	return allContacts

def getFacts(fileName):
	f = open(fileName, 'r')
	facts = f.readlines()
	i = random.randint(0, len(facts) - 1)
	return facts[i].rstrip('\n')


def send_sms(to, from_, message):
	#args = "python send_sms.py " + to + " " + from_ + " " + message
	#send_sms.send_sms(to, from_, message)
	#print args
	#os.system(args)

	gmailAddress = "catsarebae71@gmail.com"
	gmailPassword = "hpolvuyeppamxiyu"
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( gmailAddress, gmailPassword )

	#print sys.argv[0], to, from_, message

	server.sendmail(from_, to, message )
	print "sent"

def sendToAll():

	contacts = parseContacts(CONTACTS_FILE)
	from_ = "CatLover"
	randFact = getFacts(FACTS_FILE)
	for i in contacts:
		to = i.numMail
		message =  "Here is your random cat fact for the hour"
		send_sms(to, from_, message)
		send_sms(to, from_, randFact)

def sendIntro():
	contacts = parseContacts(CONTACTS_FILE)
	from_ = "CatLover"
	randFact = getFacts(FACTS_FILE)
	for i in contacts:
		to = i.numMail
		message =  "Thanks for subscribing to random cat facts.  You will recive a cat fact every hour!"
		send_sms(to, from_, message)



to = "5127799193@messaging.sprintpcs.com"
from_ = "CAT"
randFact = getFacts(FACTS_FILE)
print randFact
message = "Thanks for subscribing to random cat facts.  You will recive a cat fact every hour!" 
#print message
#send_sms(to, from_, message)
send_sms(to, from_, randFact)


