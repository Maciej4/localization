import csv

row0 = ['2', ' Marie', ' California']
row1 = ['3', ' Despacito', ' Germany']

#with open('people.csv', 'r') as readFile:
#reader = csv.reader(readFile)
#lines = list(reader)
#lines[2] = row

with open('train_data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(row0)
    writer.writerow(row1)

#readFile.close()
writeFile.close()
