import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ad1 = dict()
ad1['name'] = 'Баф HAD салатовий туристичний'
ad1['category'] = 'ТУРИЗМ'
ad1['description'] = 'Баф HAD салатовий туристичний\n\nСамовивіз або доставка Новою Поштою\n' \
                     'За потреби зроблю заміри, пишіть :)'
ad1['price'] = '40'
ad1['weight'] = '0-0.5 кг'
ad1['private or business'] = '0'
ad1['state'] = '0'
ad1['number of photos'] = '2'

dict_data = list()
csv_columns = list(ad1.keys())
dict_data.append(ad1)

csv_file = "Adverts.csv"
try:
    with open(csv_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(ad1)
