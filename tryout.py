# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# options = Options()
# options.add_argument("--window-size=1920x1080")
# options.add_argument("--verbose")

# DRIVER_BIN = '/Users/saujanyathapaliya/Documents/chromedriver_mac64/chromedriver'

# driver = webdriver.Chrome()
# driver.get("https://www.saharshatiwari.com.np")

import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
lines_with_code = [tag for tag in soup.find_all(True) if tag.find('code')]

for line in lines_with_code:
    print(line)



