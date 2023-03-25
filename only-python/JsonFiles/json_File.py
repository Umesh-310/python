import json

jsonFile = open('json_File.txt', 'r')

file_content = json.load(jsonFile)

jsonFile.close()

print(file_content['friend'][1])

Aku = [
    {'name': 'Aku', 'age': 22},
    {'name': 'Umesh', 'age': 21}
]


with open('we.txt', 'w') as file:
    json.dump(Aku, file)

with open('we.txt', 'r') as file_r:
    print(file_r.read())
