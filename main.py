import play_scraper
from play_scraper import lists
import time

f = open('result.txt','w')

scraper = play_scraper.collection(
    collection='TRENDING',
    results = 10,
    page = 0

)

list_of_ids = []
list_of_emails = []
for item in scraper:
    list_of_ids.append(item['app_id'])

# print(list_of_ids)

for id in list_of_ids:
    a = play_scraper.details(id)['developer_email']
    print(a)
    f.write(str(a)+',\n')
    list_of_emails.append(a)

