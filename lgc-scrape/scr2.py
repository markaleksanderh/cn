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
# This grabs only the relevant h3 tags
h3_soup = gov_soup.findAll('h3', {'class': 'gem-c-document-list__item-title'})

# Now loop through array of h3 elements
for a in h3_soup:
	print(a.find('a'))


# href attribute of anchor tags is relative so to get the scraper to work,
# be sure to provide the rest of the url
base_url = ''
