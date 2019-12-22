import csv
import os

with open('coors.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = dict((rows[0], rows[1]) for rows in reader)


file_path = os.path.join('..', 'csv2')