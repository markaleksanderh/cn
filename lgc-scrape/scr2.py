# from bs4 import BeautifulSoup
#
# import requests
# import urllib
#
# url = ("https://www.gov.uk/government/collections/workforce-management")
#
# r  = requests.get(url)
#
# ##data = url.text
#
# soup = BeautifulSoup(url)
# link = soup.find('a', href=True)
#
# for link in soup.find_all("a"):
# 	print(link.get('href'))


import requests
from bs4 import BeautifulSoup

# Store scraped URLs in array
next_page_urls = []

# Request content of following URL as string
gov_req = requests.get('https://www.gov.uk/government/collections/workforce-management').content

# Parse string using BeautifulSoup specifying html.parser as parser
gov_soup = BeautifulSoup(gov_req, 'html.parser')

# Anchor tags don't have classes so select parent element then select anchor child element after
# First, find all h3 tags with class 'gem-c-document-list__item-title'
h3_soup = gov_soup.findAll('h3', {'class': 'gem-c-document-list__item-title'})

for a in h3_soup:
	print(a.find('a'))


# href attribute of anchor tags is relative so to get the scraper to work,
# be sure to provide the rest of the url
base_url = ''
#
# print(child_anchor_element)
