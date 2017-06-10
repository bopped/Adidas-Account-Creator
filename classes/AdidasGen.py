import time, random, string, os, sys
from bs4 import BeautifulSoup
from colorama import *
init()
from GmailDotGen import GmailDotEmailGenerator

class AccountGEN:

	def __init__(self, s, config):
		self.s = s
		self.config = config

	def log(self, msg, Color = ""):
		currenttime = time.strftime("%H:%M:%S")
		sys.stdout.write("[%s]%s %s\n" % (currenttime,Color, str(msg) + Style.RESET_ALL))
		sys.stdout.flush()

	def AccountCheck(self, response):
		try:
			return True if (BeautifulSoup(response.text, "html.parser").find('input', {'name': 'username'})['value'] != "") else False
		except:
			return False

	def POST(self, s, URL, payload = ""):
		resp   = s.post(URL,data=payload)

		if self.AccountCheck(resp):
			return True

		elif not self.AccountCheck(resp):
			return False


			
	def US(self, s, data, NumberofAccounts):
		RandPass    = False
		error       = Fore.RED
		success     = Fore.GREEN
		info        = Fore.BLUE
		FirstName   = data['INFO']['First_Name']
		LastName    = data['INFO']['Last_Name']
		Month       = data['INFO']['Month']
		Day         = data['INFO']['Day']
		Year        = data['INFO']['Year']
		Email       = data['INFO']['Email']
		Password    = data['INFO']['Password']

		if Password  == "":
			RandPass = True

		if "gmail" not in Email.split('@')[1]:
			self.log("Sorry This Domain: %s is not Supported!!!" % (Email.split('@')[1]),error)
			exit()

		self.log("-------------------------------",info)
		self.log('ADIDAS US | Generator',success)
		self.log("First Name: %s" % (FirstName))
		self.log("Last Name: %s"  % (LastName))
		self.log("Date Of Birth: {Month: %s} {Day: %s} {Year: %s} " % (Month,Day,Year))
		self.log("Using Email: %s" % (Email.split("@")[0]))
		self.log('Password Usage: %s' % (Password if Password != '' else "Random Passwords"))
		self.log("-------------------------------",info)
		for email in (GmailDotEmailGenerator(Email).generate())[:NumberofAccounts]:
			headers = {
							  'User-Agent'               : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
							  'Accept-Encoding'          : 'gzip, deflate, sdch, br',
							  'Accept-Language'          : 'en-US,en;q=0.8',
							  'Upgrade-Insecure-Requests': '1'
					}

			s.headers.update(headers)
			try:
				GETCSRF      = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
				CSRF         = BeautifulSoup(GETCSRF.text, "html.parser").find('input', {'name': 'CSRFToken'})['value']
			except:
				self.log("Could not grab Token! Possible you're Banned!")
			s.headers.update({
							  'Origin' : 'https://cp.adidas.com',
							  'Referer': 'https://cp.adidas.com/web/eCom/en_US/loadcreateaccount'})
			if RandPass:
				length      = 13
				chars       = string.ascii_letters + string.digits + '$&@?!#%'
				random.seed = (os.urandom(1024))
				Password    = ''.join(random.choice(chars) for i in range(length))

			POSTDATA     =   {
				'firstName'                                     : FirstName,
				'lastName'                                      : LastName,
				'minAgeCheck'                                   : 'true',
				'_minAgeCheck'                                  : 'on',
				'email'                                         : email,
				'password'                                      : Password,
				'confirmPassword'                               : Password,
				'_amf'                                          : 'on',
				'terms'                                         : 'true',
				'_terms'                                        : 'on',
				'metaAttrs[pageLoadedEarlier]'                  : 'true',
				'app'                                           : 'eCom',
				'locale'                                        : 'en_US',
				'domain'                                        : '',
				'consentData1'                                  : 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
				'consentData2'                                  : '',
				'consentData3'                                  : '',
				'CSRFToken'                                     : CSRF
							   }

			URL           = 'https://cp.adidas.com/web/eCom/en_US/accountcreate'
			AccountStatus = self.POST(s, URL, payload=POSTDATA)

			if AccountStatus:
				self.log("Account Created Successfully! Email: %s. Password: %s" % (email,Password),success)
				with open('accounts' + '.txt', 'a') as f:
					f.write('%s:%s \n' % (email,Password))
					f.close()
				Sleep = (random.randint(2, 10))
				self.log("Sleeping for %d seconds" % (Sleep),info)
				time.sleep(Sleep)


			if not AccountStatus:
				self.log("Account could not be created! Email: %s. Password: %s" % (email,Password),error)

			s.cookies.clear()

	def UK(self, s, data, NumberofAccounts):

		RandPass    = False
		error       = Fore.RED
		success     = Fore.GREEN
		info        = Fore.BLUE
		FirstName   = data['INFO']['First_Name']
		LastName    = data['INFO']['Last_Name']
		Month       = data['INFO']['Month']
		Day         = data['INFO']['Day']
		Year        = data['INFO']['Year']
		Email       = data['INFO']['Email']
		Password    = data['INFO']['Password']

		if Password  == "":
			RandPass = True

		if "gmail" not in Email.split('@')[1]:
			self.log("Sorry This Domain: %s is not Supported!!!" % (Email.split('@')[1]),error)
			exit()

		self.log("-------------------------------", info)
		self.log('ADIDAS UK | Generator',success)
		self.log("First Name: %s" % (FirstName))
		self.log("Last Name: %s"  % (LastName))
		self.log("Date Of Birth: {Month: %s} {Day: %s} {Year: %s} " % (Month,Day,Year))
		self.log("Using Email: %s" % (Email.split("@")[0]))
		self.log('Password Usage: %s' % (Password if Password != '' else "Random Passwords"))
		self.log("-------------------------------", info)
		for email in (GmailDotEmailGenerator(Email).generate())[:NumberofAccounts]:
			headers = {
							  'User-Agent'               : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
							  'Accept-Encoding'          : 'gzip, deflate, sdch, br',
							  'Accept-Language'          : 'en-US,en;q=0.8',
							  'Upgrade-Insecure-Requests': '1'
					}

			s.headers.update(headers)
			try:
				GETCSRF      = s.get('https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount')
				CSRF         = BeautifulSoup(GETCSRF.text, "html.parser").find('input', {'name': 'CSRFToken'})['value']
			except:
				self.log("Could not grab Token! Possible you're Banned!")
			s.headers.update({
				'Origin': 'https://cp.adidas.co.uk',
				'Referer': 'https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount'})

			if RandPass:
				length      = 13
				chars       = string.ascii_letters + string.digits + '$&@?!#%'
				random.seed = (os.urandom(1024))
				Password    = ''.join(random.choice(chars) for i in range(length))

			POSTDATA     =   {
					   'firstName'                      : FirstName,
					   'lastName'                       : LastName,
					   'minAgeCheck'                    : 'true',
					   'day'                            : Day,
					   'month'                          : Month,
					   'year'                           : Year,
					   '_minAgeCheck'                   : 'on',
					   'email'                          : email,
					   'password'                       : Password,
					   'confirmPassword'                : Password,
					   '_amf'                           : 'on',
					   'terms'                          : 'true',
					   '_terms'                         : 'on',
					   'metaAttrs[pageLoadedEarlier]'   : 'true',
					   'app'                            : 'eCom',
					   'locale'                         : 'en_GB',
					   'domain'                         : '',
					   'consentData1'                   : 'Sign me up for adidas emails, featuring exclGBive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.co.uk/GB/help-topics-privacy_policy.html">Policy Policy</a> for details.',
					   'consentData2'                   : '',
					   'consentData3'                   : '',
					   'CSRFToken'                      : CSRF
							   }

			URL           = 'https://cp.adidas.co.uk/web/eCom/en_GB/accountcreate'
			
			AccountStatus = self.POST(s, URL, payload=POSTDATA)

			if AccountStatus:
				self.log("Account Created Successfully! Email: %s. Password: %s" % (email,Password),success)
				with open('accounts' + '.txt', 'a') as f:
					f.write('%s:%s\n' % (email,Password))
					f.close()
				Sleep = (random.randint(2, 10))
				self.log("Sleeping for %d seconds" % (Sleep),info)
				time.sleep(Sleep)


			if not AccountStatus:
				self.log("Account could not be created! Email: %s. Password: %s" % (email,Password),error)

			s.cookies.clear()


	def AU(self, s, data, NumberofAccounts):
			RandPass    = False
			error       = Fore.RED
			success     = Fore.GREEN
			info        = Fore.BLUE
			FirstName   = data['INFO']['First_Name']
			LastName    = data['INFO']['Last_Name']
			Month       = data['INFO']['Month']
			Day         = data['INFO']['Day']
			Year        = data['INFO']['Year']
			Email       = data['INFO']['Email']
			Password    = data['INFO']['Password']

			if Password  == "":
				RandPass = True

			if "gmail" not in Email.split('@')[1]:
				self.log("Sorry This Domain: %s is not Supported!!!" % (Email.split('@')[1]),error)
				exit()

			self.log("-------------------------------", info)
			self.log('ADIDAS AU | Account Generator',success)
			self.log("First Name: %s" % (FirstName))
			self.log("Last Name: %s"  % (LastName))
			self.log("Date Of Birth: {Month: %s} {Day: %s} {Year: %s} " % (Month,Day,Year))
			self.log("Using Email: %s" % (Email.split("@")[0]))
			self.log('Password Usage: %s' % (Password if Password != '' else "Random Passwords"))
			self.log("-------------------------------\n", info)
			for email in (GmailDotEmailGenerator(Email).generate())[:NumberofAccounts]:
				headers = {
								  'User-Agent'               : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
								  'Accept-Encoding'          : 'gzip, deflate, sdch, br',
								  'Accept-Language'          : 'en-US,en;q=0.8',
								  'Upgrade-Insecure-Requests': '1'
						}

				s.headers.update(headers)
				try:
					GETCSRF      = s.get('https://cp.adidas.com/web/eCom/en_AU/loadcreateaccount')
					CSRF         = BeautifulSoup(GETCSRF.text, "html.parser").find('input', {'name': 'CSRFToken'})['value']
				except:
					self.log("Could not grab Token! Possible you're Banned!")
				s.headers.update({
					'Origin': 'https://cp.adidas.com',
					'Referer': 'https://cp.adidas.com/web/eCom/en_AU/loadcreateaccount'})

				if RandPass:
					length      = 13
					chars       = string.ascii_letters + string.digits + '$&@?!#%'
					random.seed = (os.urandom(1024))
					Password    = ''.join(random.choice(chars) for i in range(length))

				POSTDATA     =   {
						   'firstName'                                   : FirstName,
						   'lastName'                                    : LastName,
						   'day'                                         : Day,
						   'month'                                       : Month,
						   'year'                                        : Year,
						   'email'                                       : email,
						   'password'                                    : Password,
						   'confirmPassword'                             : Password,
						   '_amf'                                        : 'on',
						   'terms'                                       : 'true',
						   '_terms'                                      : 'on',
						   'metaAttrs[pageLoadedEarlier]'                : 'true',
						   'app'                                         : 'eCom',
						   'locale'                                      : 'en_AU',
						   'domain'                                      : '',
						   'consentData1'                                : 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
						   'consentData2'                                : '',
						   'consentData3'                                : '',
						   'CSRFToken'                                   : CSRF
								   }

				URL           = 'https://cp.adidas.com/web/eCom/en_AU/accountcreate'

				AccountStatus = self.POST(s, URL, payload=POSTDATA)

				if AccountStatus:
					self.log("Account Created Successfully! Email: %s. Password: %s" % (email,Password),success)
					with open('accounts' + '.txt', 'a') as f:
						f.write('%s:%s\n' % (email, Password))
						f.close()
					Sleep = (random.randint(2, 10))
					self.log("Sleeping for %d seconds" % (Sleep),info)
					time.sleep(Sleep)


				if not AccountStatus:
					self.log("Account could not be created! Email: %s. Password: %s" % (email,Password),error)

				s.cookies.clear()
	def CA(self, s, data, NumberofAccounts):
			RandPass    = False
			error       = Fore.RED
			success     = Fore.GREEN
			info        = Fore.BLUE
			FirstName   = data['INFO']['First_Name']
			LastName    = data['INFO']['Last_Name']
			Month       = data['INFO']['Month']
			Day         = data['INFO']['Day']
			Year        = data['INFO']['Year']
			Email       = data['INFO']['Email']
			Password    = data['INFO']['Password']

			if Password  == "":
				RandPass = True

			if "gmail" not in Email.split('@')[1]:
				self.log("Sorry This Domain: %s is not Supported!!!" % (Email.split('@')[1]),error)
				exit()

			self.log("-------------------------------", info)
			self.log('ADIDAS CA | Account Generator',success)
			self.log("First Name: %s" % (FirstName))
			self.log("Last Name: %s"  % (LastName))
			self.log("Date Of Birth: {Month: %s} {Day: %s} {Year: %s} " % (Month,Day,Year))
			self.log("Using Email: %s" % (Email.split("@")[0]))
			self.log('Password Usage: %s' % (Password if Password != '' else "Random Passwords"))
			self.log("-------------------------------", info)
			for email in (GmailDotEmailGenerator(Email).generate())[:NumberofAccounts]:
				headers = {
								  'User-Agent'               : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
								  'Accept-Encoding'          : 'gzip, deflate, sdch, br',
								  'Accept-Language'          : 'en-US,en;q=0.8',
								  'Upgrade-Insecure-Requests': '1'
						}

				s.headers.update(headers)
				try:
					GETCSRF      = s.get('https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount')
					CSRF         = BeautifulSoup(GETCSRF.text, "html.parser").find('input', {'name': 'CSRFToken'})['value']
				except:
					self.log("Could not grab Token! Possible you're Banned!")

				s.headers.update({
					'Origin': 'https://cp.adidas.ca',
					'Referer': 'https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount'})


				if RandPass:
					length      = 13
					chars       = string.ascii_letters + string.digits + '$&@?!#%'
					random.seed = (os.urandom(1024))
					Password    = ''.join(random.choice(chars) for i in range(length))

				POSTDATA     =   {
						   'firstName'                                          : FirstName,
						   'lastName'                                           : LastName,
						   'minAgeCheck'                                        : 'true',
						   '_minAgeCheck'                                       : 'on',
						   'email'                                              : email,
						   'password'                                           : Password,
						   'confirmPassword'                                    : Password,
						   'amf'                                                : 'true',
						   '_amf'                                               : 'on',
						   'terms'                                              : 'true',
						   '_terms'                                             : 'on',
						   'metaAttrs[pageLoadedEarlier]'                       : 'true',
						   'app'                                                : 'eCom',
						   'locale'                                             : 'en_CA',
						   'domain'                                             : '',
						   'consentData1'                                       : 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
						   'consentData2'                                       : 'By entering my information, I give permission for adidas Canada Limited to contact me in future for marketing, advertising and oaS pinion research for purposes of the adidas Group. I understand I can later withdraw consent.<a target="_blank" href="http://www.adidas.ca/en/help-topics-privacy_policy.html"><b>Learn More</b></a',
						   'consentData3'                                       : '',
						   'CSRFToken'                                          : CSRF
								   }

				URL           = 'https://cp.adidas.ca/web/eCom/en_CA/accountcreate'

				AccountStatus = self.POST(s, URL, payload=POSTDATA)

				if AccountStatus:
					self.log("Account Created Successfully! Email: %s. Password: %s" % (email,Password),success)
					with open('accounts' + '.txt', 'a') as f:
						f.write('%s:%s\n' % (email, Password))
						f.close()
					Sleep = (random.randint(2, 10))
					self.log("Sleeping for %d seconds" % (Sleep),info)
					time.sleep(Sleep)


				if not AccountStatus:
					self.log("Account could not be created! Email: %s. Password: %s" % (email,Password),error)

				s.cookies.clear()



if __name__ == '__main__':
	print "DO NOT RUN THIS FILE!!!!!"
	#exit()
