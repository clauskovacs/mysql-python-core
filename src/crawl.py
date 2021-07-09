# -*- coding: utf-8 -*-
#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class crawler:
	"""This class contains all functions responsible for crawling webpages.

	All functions build upon webdriver to fetch pages. Among other things,
	the functions in this class are responsible for initiing and closing 
	the webdriver, fetching webpages, etc.
	"""
	def __init__(self, run_headless, non_headless_width, non_headless_height):
		"""The constructor which sets the parameters regarding the webdriver.

		If run_headless is True, webdriver will run in
		headless mode, i.e., no browser window will open
		during program runtime. In case the option is set
		to False, the other two variables define the height
		and width of the the browser window.
		"""
		self.headless = run_headless						# True ... run in headless mode
		self.non_headless_height = non_headless_height		# height of the browser window (if run_headless == False)
		self.non_headless_width = non_headless_width		# width of the browser window (if run_headless == False)

	def init_driver(self):
		"""Initiate the webdriver (as defined by the user).

		Using the provided options (headlessness, user agent, browser
		window height and width, etc.), this function initiates the
		webdriver.		
		"""
		print ('initing driver')

		# browser options for chrome
		chrome_options = Options()
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument("--no-sandbox") # linux only
		#chrome_options.add_experimental_option("detach", True)

		# option for running headless (opening a visible browser window or not)
		if self.headless == True:
			chrome_options.add_argument("--headless")

		# set the user agent
		chrome_options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

		# set the driver (chrome)
		driver = webdriver.Chrome(options = chrome_options)

		# set the browser window size (if run_headless == False)
		if self.headless == False:
			driver.set_window_size(self.non_headless_width, self.non_headless_height)

		"""
		Return the handle to keep the browser open over the span
		of the program (else each function call would open and
		close the browser completely)
		"""
		return driver

	def close_driver(self, driver):
		'''Close the webdriver properly.'''
		print ('closing driver')

		driver.close()	# close the current browser window
		driver.quit()	# calls driver.dispose which closes all the browser windows and ends the webdriver session properly

	def fetch_page(self, driver):
		'''Fetches a single website using webdriver.'''
		print ('fetching page')

		# fetch the page (open the headless browser)
		#driver.get("https://tiss.tuwien.ac.at/course/courseDetails.xhtml?dswid=2327&dsrid=104&courseNr=242023&semester=2021S")
		driver.get("https://webscraper.io/test-sites/e-commerce/allinone")

		"""
		Wait until the javascript code has been delivered. If this
		waiting time is not set, the retrieved page is faulty, i.e., it
		will contain a warning to 'enable JS'. This is due to the fact that
		the page sets a JS cookie, reloads/redirects and this must be resolved
		before fetching the page or it (the fetching) will not succeed!
		"""
		sleep(2)

		"""
		TODO: ensure, the page has been retrieved properly, e.g., search
		through the source code for the warning to enable JS. In that case
		the page has not been fetched properly, the waiting time must be
		increased and the page must be re-fetched.
		"""

		# fetch the contents in the targed div (id = contentInner)
		#html = driver.execute_script('return window.document.getElementById("contentInner").innerHTML')
		#print(html)
