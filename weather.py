#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 9 part 3 for IS211"""


from bs4 import BeautifulSoup
import urllib2
import re


r = urllib2.urlopen("https://www.wunderground.com/history/airport/KNYC/2015/1/1/MonthlyHistory.html").read()

soup = BeautifulSoup(r, "html.parser")
table = soup.find('table', attrs={"id": "obsTable"})
table_row = table.findAll('tr')

print "\n Actual and forecasted weather for the days in the month of January 2015 \n"

for tr in table_row:

    try:
        date = tr.find(href=re.compile('/history/airport/KNYC/2015/1'))
        print "January " + date.text + ", 2015"

    except AttributeError:
        pass

    try:
        td = tr.findAll('span')
        high = td[0]
        avg = td[1]
        low = td[2]
        print "High " + high.text, "Average " + avg.text, "Low " + low.text
        print '-' * 120

    except IndexError:
        pass
