from selenium import webdriver
import time
from bs4 import BeautifulSoup, SoupStrainer
from tqdm import tqdm
import requests
import re
import os.path 
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
my_dates = []
txt_file = open("Date.txt", "w")
my_links = open('output.txt').readlines()
for url in tqdm(my_links[1:]):
	driver = webdriver.Firefox(options = options)
	driver.get(url)

	driver.implicitly_wait(1)
	content = driver.page_source
	date_idx = content.find('<span class=\"date\"')
	date = content[date_idx+19:date_idx + 31]
	txt_file.write(date+"\n")
	#my_dates.append(date)
'''
with open("Date.txt", "w") as txt_file:
	for line in my_links:
		txt_file.write("".join(line) + "\n")
'''

#print content
#print(content)
