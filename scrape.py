import os
import requests
from bs4 import BeautifulSoup

open('headlines.txt', 'w').close()


# Refactor Building.co.uk headlines


building_news = requests.get('http://www.building.co.uk/').content
bld_soup = BeautifulSoup(building_news, 'html.parser')
bld_headlines = bld_soup.findAll('h2')


enquirer = requests.get('http://www.constructionenquirer.com/').content
enq_soup = BeautifulSoup(enquirer, 'html.parser')
enq_headlines = enq_soup.findAll('h3')

with open('headlines.txt', 'wt') as output:

    output.write('Building.co.uk headlines:\n')
    print('Building.co.uk headlines:\n')
    for i in range(1, 6):
        output.write('{}\n'.format(bld_headlines[i].contents[0].string))
        print('{}\n'.format(bld_headlines[i].contents[0].string))

    output.write('\nConstruction Enquirer headlines:\n')
    print('\nConstruction Enquirer headlines:\n')
    for i in range(1, 6):
        output.write('{}\n'.format(enq_headlines[i].contents[0].string))
        print('{}\n'.format(enq_headlines[i].contents[0].string))


os.system('start headlines.txt')
