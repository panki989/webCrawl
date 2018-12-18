#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from bs4 import Doctype

#url = 'https://www.w3.org'
url2 = 'https://www.w3.org/TR/html4/struct/links.html'
page = requests.get(url2)
soup = BeautifulSoup(page.text, 'lxml')

items = [item for item in soup.contents if isinstance(item, Doctype)]
data = items[0] if items else None

print(data)
