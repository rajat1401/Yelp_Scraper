import csv
import json

with open("scraped_businesses.json", "r") as f:
    data= json.load(f)
print  (len(data))

f= csv.writer(open('scraped_businesses.csv', "w"))
f.writerow(['name', 'address', 'categories', 'zip_code', 'phone', 'rating', 'url'])
for business in data:
    f.writerow([business['name'], business['address'], business['categories'], business['zip_code'], business['phone'], business['rating'], business['url']])
    