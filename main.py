import play_scraper
import time

f = open('result.txt', 'w')

scraper = play_scraper.collection(
    collection='TRENDING',
    results=10,
    page=0

)

list_of_ids = []
list_of_details = []
for item in scraper:
    list_of_ids.append(item['app_id'])

# print(list_of_ids)

for id in list_of_ids:
    a = play_scraper.details(id)
    b = {a['app_id']: [a['title'], a['developer_id'], a['installs'], a['developer_url'], a['developer_email']]}
    list_of_details.append(b)
    f.write(str(b) + '\n')

print(list_of_details)
