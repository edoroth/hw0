import csv

key = 'SINGLE MALT SCOTCH'

csvfile = open('iowa-liquor-sample.csv', 'rb')
myreader = csv.reader(csvfile)
count = 0
for row in myreader:
	if key in row[11].upper() or key in row[15].upper() :
		count += 1
print count

