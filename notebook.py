import numpy as np
import pandas as pd
import unicodecsv as csv
import requests
import csv
import argparse
import json
import re
from lxml import html


def get_businesses(location, term, api_key):
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'

    data = []
    for offset in range(0, 1000, 50):
        print ("Going")
        params = {
            'limit': 50, 
            'location': location.replace(' ', '+'),
            'term': term.replace(' ', '+'),
            'offset': offset
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            # data+= response.json()['businesses']
            for business in response.json()['businesses']:
                try:
                    data.append({
                        "name": business['name'],
                        "address": business["location"]['address1'],
                        "categories": [item['title'] for item in business['categories']],
                        "zip_code": business['location']['zip_code'],
                        "phone": business['display_phone'], 
                        "rating": business['rating'],
                        "url": business['url']
                    })
                except Exception as e:
                    print (e)
        elif response.status_code == 400:
            print('400 Bad Request')
            break
    print (len(data))
    # print (data[:10])
    f= csv.writer(open('scraped_businesses.csv', "w"))
    f.writerow(['name', 'address', 'categories', 'zip_code', 'phone', 'rating', 'url'])
    for business in data:
        f.writerow([business['name'], business['address'], business['categories'], business['zip_code'], business['phone'], business['rating'], business['url']])
