# TEST
# Importing libraries
import time
import hashlib
import smtplib
from urllib.request import urlopen, Request
from settings import USR, PASS, RCPT

# setting the URL you want to monitor
url = Request('APPLY WEBSITE TO MONITOR FOR CHANGES HERE',
			headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("Scanning for changes...")
time.sleep(10)
while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()
		
		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 120 seconds
		time.sleep(120)
		
		# perform the get request
		response = urlopen(url).read()
		
		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash
		if newHash == currentHash:
			continue

		# if something changed in the hashes
		else:
			# notify
			print("Something changed!")
			time.sleep(1)
			try:
				# =============================================================================
				# SET EMAIL LOGIN REQUIREMENTS
				# =============================================================================
				gmail_user = USR
				gmail_app_password = PASS
				gmail_receipt = RCPT

				# =============================================================================
				# SET THE INFO ABOUT EMAIL
				# =============================================================================
				sent_from = gmail_user
				sent_to = gmail_receipt
				sent_subject = "HAVE A SUBJECT HERE"
				sent_body = ("PUT YOUR EMAIL HERE\n"
							 "GIVE IT SOME MORE AND APPRECIATE\n"
							 "\n"
							 "CHEER THE MAIL\n")

				email_text = """\
				From: %s
				Subject: %s

				%s
				""" % (sent_from, sent_subject, sent_body)

				# =============================================================================
				# SEND EMAIL OR DIE TRYING!!!
				# =============================================================================

				try:
					server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
					server_ssl.ehlo()
					server_ssl.login(gmail_user, gmail_app_password)
					server_ssl.sendmail(sent_from, sent_to, email_text)
					server_ssl.close()

					print('Email sent!')
				except Exception as exception:
					print("Error: %s!\n\n" % exception)
			except:
				print('No Mail sent, something was weird...')

			# again read the website
			response = urlopen(url).read()

			# create a hash
			currentHash = hashlib.sha224(response).hexdigest()

			# wait for 30 seconds
			time.sleep(30)
			continue
			
	# To handle exceptions
	except Exception as e:
		print("Error")
