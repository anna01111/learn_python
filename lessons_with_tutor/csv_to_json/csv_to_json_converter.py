import csv
import json

# read data from csv_file.txt
with open('csv_to_json/csv_file.txt', 'r') as f:
    reader = list(csv.reader(f))
print(reader)

# process data and convert them into a single JSON object
keys = ['club', 'city', 'country']
json_object = []
for el in reader:
    new_el = dict(zip(keys, el))
    json_object.append(new_el)
print(json_object)

# store the JSON object into json_file.txt
with open('csv_to_json/json_file.txt', 'w') as f:
    writer = json.dump(json_object, f)



