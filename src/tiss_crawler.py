# -*- coding: utf-8 -*-
#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# browser options for chrome
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")


# change the user agent
chrome_options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# set the driver (chrome)
driver = webdriver.Chrome(options = chrome_options)

# set the browser size (for the non-headless version)
#driver.set_window_size(800, 600)

# fetch the page (open the headless browser)
driver.get("https://tiss.tuwien.ac.at/course/courseDetails.xhtml?dswid=2327&dsrid=104&courseNr=242023&semester=2021S")

# wait until the javascript code has been delivered
sleep(2)

# fetch the contents in the targed div (id = contentInner)
html = driver.execute_script('return window.document.getElementById("contentInner").innerHTML')
print(html)


driver.close()	# close the current browser window
driver.quit()	# calls driver.dispose which closes all the browser windows and ends the WebDriver session properly
