import csv

data = [
    ['Temperature', 'CustomerCount', 'Revenue'],
    ['2021-01-01', 25.3, 50, 250.00],
    ['2021-01-02', 22.1, 45, 225.50],
    ['2021-01-03', 24.5, 55, 275.00],
    ['2021-01-04', 26.8, 60, 300.00],
    ['2021-01-05', 20.7, 40, 200.00]
]

filename = 'lemonade_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)