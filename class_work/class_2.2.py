import csv, json, yaml
from pprint import pprint

# with open('data/read.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# with open('data/read.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
# with open('data/read.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row.get('header1'))
#
# data = [['header1', ' header2', ' header3', ' header4'],
# ['data1', ' data2', ' data3', ' data4'],
# ['data1', ' data2', ' data3', ' data4'],
# ['data1', ' data2', ' data3', ' data4'],
# ['data1', ' data2', ' data3', ' data4'],
# ['data1', ' data2', ' data3', ' data4'],
# ['data1', ' data2', ' data3', ' data4']]
#
# with open('data/write.csv', 'w') as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)

# data = [{'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
#          {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'}]
# #
# headers =  ['header1', 'header2', 'header3', 'header4']
# with open('data/write.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)
#
# with open('data/read.json') as file:
#
#
# with open('data/read.json') as file:
#     raw = file.read()
#     pprint(json.loads(raw))
# with open('data/write.json', 'w') as file:
#     json.dump(data, file, indent=4)
# with open('data/read.yml') as file:
#     pprint(
#         yaml.load(file, Loader=yaml.Loader)
#     )
data = {
    'attr1': 'value1',
    'attr2': 'value2',
    'attr3': 'value3',
    'attr4': ['value1', 'value2', 'value3']
}
with open('data/write.yml', 'w') as file:
    yaml.dump(data, file, Dumper=yaml.Dumper)

