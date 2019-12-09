from tabulate import tabulate

list = [['Python', 'interpreted', '1991'],
                ['JAVA', 'compiled', '1995'],
                ['С', 'compiled', '1972']]
data = [{'name': 'Python', 'type': 'interpreted', 'year': '1991' },
        {'name': 'Python', 'type': 'interpreted', 'year': '1991' },
        {'name': 'Python', 'type': 'interpreted', 'year': '1991' }]
columns = ['name', 'type', 'year']

print(tabulate(data, headers='keys'))

print(tabulate(data, headers='keys', tablefmt='grid'))

print(tabulate(data, headers='keys', tablefmt='html'))