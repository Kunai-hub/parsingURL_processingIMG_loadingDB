# -*- coding: utf-8 -*-

import requests


html = requests.get(r'https://skillbox.ru/course/profession-python/').text


print(html)
