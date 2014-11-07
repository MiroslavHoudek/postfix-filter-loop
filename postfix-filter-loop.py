import smtpd
import asyncore

import smtplib

import traceback

class CustomSMTPServer(smtpd.SMTPServer):

	def process_message(self, peer, mailfrom, rcpttos, data):
		
		mailfrom.replace('\'', '')
		mailfrom.replace('\"', '')
		
		for recipient in rcpttos:
			recipient.replace('\'', '')
			recipient.replace('\"', '')
		
#		print 'Receiving message from:', peer
#		print 'Message addressed from:', mailfrom
#		print 'Message addressed to  :', rcpttos
#		print 'MSG >>'
#		print data
#		print '>> EOT'

		try:
			# DO WHAT YOU WANNA DO WITH THE EMAIL HERE
			# I'd like to include some more functions for users convenience, such as 
			# functions to change fields within the body (From, Reply-to etc), 
			# and/or to send error codes back to Postfix.
		
			pass
		except:
			pass
			print 'Something went south'
			print traceback.format_exc()

		try:
			server = smtplib.SMTP('localhost', 10026)
			server.sendmail(mailfrom, rcpttos, data)
			server.quit()
#			print 'send successful'
		except smtplib.SMTPException:
			print 'Exception SMTPException'
			pass
		except smtplib.SMTPServerDisconnected:
			print 'Exception SMTPServerDisconnected'
			pass
		except smtplib.SMTPResponseException:
			print 'Exception SMTPResponseException'
			pass		
		except smtplib.SMTPSenderRefused:
			print 'Exception SMTPSenderRefused'
			pass		
		except smtplib.SMTPRecipientsRefused:
			print 'Exception SMTPRecipientsRefused'
			pass		
		except smtplib.SMTPDataError:
			print 'Exception SMTPDataError'
			pass		
		except smtplib.SMTPConnectError:
			print 'Exception SMTPConnectError'
			pass		
		except smtplib.SMTPHeloError:
			print 'Exception SMTPHeloError'
			pass		
		except smtplib.SMTPAuthenticationError:
			print 'Exception SMTPAuthenticationError'
			pass
		except:
			print 'Undefined exception'
			print traceback.format_exc()

		return
		
server = CustomSMTPServer(('127.0.0.1', 10025), None)

asyncore.loop()
