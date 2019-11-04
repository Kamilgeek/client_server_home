import csv

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

data = [{'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'},
         {'header1': 'data1', 'header2' : 'data2', 'header3' : 'data3', 'header4' : 'data4'}]

headers =  ['header1', 'header2', 'header3', 'header4']
with open('data/write.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
