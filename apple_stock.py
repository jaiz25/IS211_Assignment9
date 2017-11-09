#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 9 part 2 for IS211"""


from bs4 import BeautifulSoup
import urllib2


r = urllib2.urlopen("https://finance.yahoo.com/quote/AAPL/history?p=AAPL").read()

soup = BeautifulSoup(r, "html.parser")

table = soup.find('table', attrs={'data-test': 'historical-prices'})
table_row = table.findAll('tr', attrs={'class': "BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"})
for tr in table_row:
    try:
        td = tr.findAll('span')
        date = td[0]
        closing_price = td[4]
        print date.text, closing_price.text
    except IndexError:
        pass
