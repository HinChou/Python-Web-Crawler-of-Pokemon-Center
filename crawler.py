# Native lib
import os
import re
import urllib
import urllib2

# Third party lib
from bs4 import BeautifulSoup

# Read the html text
url = 'http://www.pokemoncenter.com/apparel/t-shirts#facet:&productBeginIndex:0&facetLimit:&orderBy:5&pageView:grid&minPrice:&maxPrice:&pageSize:&'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()
response.close()

# Massage the html text
soup = BeautifulSoup(html, 'html.parser')
product_names_arr = soup.find_all('div', class_ = 'product_name')
product_prices_arr = soup.find_all('div', class_ = 'product_price')
arr_length = len(product_prices_arr)
for i in xrange(0, arr_length - 1):
  product_name = product_names_arr[i].find_all(text = True)
  product_price = product_prices_arr[i].find_all(text = True)

  if (len(product_name) > 0):
    print(product_name[-2])
    print(product_price[-6])
    print('--------------------')

# Write the data
# file = 'result.txt'
# path_to_save = os.getcwd() + '/py-crawler/'
# fh = open(path_to_save + file, 'w')
# fh.write(product_names)
# fh.close()