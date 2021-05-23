# -*- coding: utf-8 -*-
#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class crawler:
	def __init__(self, run_headless, non_headless_width, non_headless_height):
		self.headless = run_headless						# True ... run in headless mode
		self.non_headless_height = non_headless_height		# height of the browser window (if run_headless == False)
		self.non_headless_width = non_headless_width		#  width of the browser window (if run_headless == False)

	# initiate the webdriver with the options for headlessness, browser window width and browser window height
	def init_driver(self):
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

		# change the user agent
		chrome_options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

		# set the driver (chrome)
		driver = webdriver.Chrome(options = chrome_options)

		# set the browser window size (if run_headless == False)
		if self.headless == False:
			driver.set_window_size(self.non_headless_width, self.non_headless_height)

		# return the handle to keep the browser open over the span of the program (else each function call would open and close the browser completely)
		return driver

	# properly close the webdriver
	def close_driver(self, driver):
		print ('closing driver')

		driver.close()	# close the current browser window
		driver.quit()	# calls driver.dispose which closes all the browser windows and ends the webdriver session properly

	# fetching a single page using the webdriver
	def fetch_page(self, driver):
		print ('fetching page')

		# fetch the page (open the headless browser)
		#driver.get("https://tiss.tuwien.ac.at/course/courseDetails.xhtml?dswid=2327&dsrid=104&courseNr=242023&semester=2021S")
		driver.get("https://webscraper.io/test-sites/e-commerce/allinone")

		# wait until the javascript code has been delivered
		sleep(2)

		# fetch the contents in the targed div (id = contentInner)
		#html = driver.execute_script('return window.document.getElementById("contentInner").innerHTML')
		#print(html)


