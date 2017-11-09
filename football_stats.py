#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 9 part 1 for IS211"""


from bs4 import BeautifulSoup
import urllib2
import re


r = urllib2.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-"
                    "touchdowns").read()


soup = BeautifulSoup(r, "html.parser")
table = soup.find('table', attrs={'class': 'data'})
table_row = table.findAll('tr', attrs={'valign': 'top'})
for tr in table_row[:20]:
    name = tr.find('td', attrs={'align': 'left'})
    pos = tr.find('td', attrs={'align': 'center'})
    team = tr.find(href=re.compile('/nfl/teams/page'))
    touchdown = tr.find('td', attrs={'class': 'sort'})
    print name.a.text, pos.text, team.text, touchdown.text



