from selenium import webdriver
import time
from bs4 import BeautifulSoup, SoupStrainer
from tqdm import tqdm
import requests
import re
import os.path 


def cleaned(url):
	req = requests.get(url)
	#print(req)
	content = req.text

	first_idx = content.find('<div class=\'news-bg\'>')
	#print(first_idx)
	end_idx = content.find('</div><div class=\"tweet-container\" >')
	#print(end_idx)

	MyText = content[first_idx:end_idx]

	CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	cleantext = re.sub(CLEANR, '',MyText)
	return cleantext


if(os.path.exists('output.txt') == False):
	url = 'https://www.pmindia.gov.in/en/mann-ki-baat/'
	my_links = []
	driver = webdriver.Firefox()
	driver.get(url)
	driver.implicitly_wait(20)
	SCROLL_PAUSE_TIME = 3

	# Get scroll height
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
	    # Scroll down to bottom
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	    # Wait to load page
	    time.sleep(SCROLL_PAUSE_TIME)

	    # Calculate new scroll height and compare with last scroll height
	    new_height = driver.execute_script("return document.body.scrollHeight")
	    if new_height == last_height:
	        break
	    last_height = new_height

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	soup_file = driver.page_source
	#print(soup_file)
	for link in BeautifulSoup(soup_file,features="lxml", parse_only = SoupStrainer('a') ):
		if link.has_attr('href'):
			if 'mann-ki-baat' in link['href']:
				my_links.append(link['href'])

	with open("output.txt", "w") as txt_file:
	    for line in my_links:
	        txt_file.write("".join(line) + "\n")
else:
	my_links = open('output.txt').readlines()
	my_links.reverse()
for i in tqdm(range(0,len(my_links)-1)):
	my_text = cleaned(my_links[i])
	file_name = 'Episode-'+str(i+1)+'.txt'
	f = open(file_name, "w", encoding = 'utf-8')
	f.write(my_text)
	f.close()




