import requests


import csv

with open('spriteLinkList.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
    
print(data[1][0])

for url in data:
	print(url[0])
	name = url[0].split("portrait/")[1].replace("/", "_")
	print(name)
	img_data = requests.get(url[0]).content
	with open("Normal/" + name, 'wb') as handler:
		handler.write(img_data)

