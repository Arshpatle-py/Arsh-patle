import json
import csv

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('data1.csv', 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("JSON data successfully converted to CSV.")
