import requests
from bs4 import BeautifulSoup

# Request content of following URL as string
gov_req = requests.get('https://www.gov.uk/government/collections/workforce-management').content

# Parse string using BeautifulSoup specifying html.parser as parser
gov_soup = BeautifulSoup(gov_req, 'html.parser')

# Anchor tags don't have classes so select parent element then select anchor child element after
# First, find all h3 tags with class 'gem-c-document-list__item-title'
# This grabs only the relevant h3 tags
h3_soup = gov_soup.findAll('h3', {'class': 'gem-c-document-list__item-title'})

# Now loop through array of h3 elements
# for a in h3_soup:
# 	next_page_urls.append(a.find('a').get('href'))

# href attribute of anchor tags is relative so to get the scraper to work,
# be sure to provide the rest of the url
base_url = 'https://www.gov.uk'



# Store scraped URLs in array
with open('urls.txt', 'wt') as outfile:
	for a in h3_soup:
		outfile.write('{}{}\n'.format(base_url, a.find('a').get('href')))

# for url in next_page_urls:
# 	print('{}{}'.format(base_url, next_page_urls))


# Open list of URLs and request each using for loop
# with open('urls.txt', 'r') as infile:
# 	first = infile.readline()
# 	print(first)
# 	csv_req = requests.get(infile.readline()).content
# 	csv_req = BeautifulSoup(csv_req, 'html.parser')
# 	# Find all span tags where class is 'download'
# 	print(csv_req.findAll('div', {'class':'attachment-details'}))
