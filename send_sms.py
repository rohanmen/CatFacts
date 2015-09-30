#http://www.example-code.com/python/sms_send.asp

#Boost Mobile: PhoneNumber@myboostmobile.com
#T-Mobile: PhoneNumber@tmomail.net
#Virgin Mobile: PhoneNumber@vmobl.com
#Cingular: PhoneNumber@cingularme.com
#Sprint Nextel: PhoneNumber@messaging.sprintpcs.com
#Verizon: PhoneNumber@vtext.com
#Nextel: PhoneNumber@messaging.nextel.com
#US Cellular: PhoneNumber@email.uscc.net
#SunCom: PhoneNumber@tms.suncom.com
#Powertel: PhoneNumber@ptel.net
#AT&T (Cingular): PhoneNumber@txt.att.net
#Alltel: PhoneNumber@message.alltel.com
#Metro PCS: PhoneNumber@MyMetroPcs.com

#make sure to turn on access to less secure apps from gmail

import sys
import smtplib

#arg[0] = scriptName
#arg[1] = to number
#arg[2] = from
#arg[3] = message


def send_sms(to, from_, message):

	print to
	print from_
	print message

	gmailAddress = "catsarebae71@gmail.com"
	gmailPassword = "hpolvuyeppamxiyu"
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( gmailAddress, gmailPassword )

	#print sys.argv[0], to, from_, message

	server.sendmail(from_, to, message )