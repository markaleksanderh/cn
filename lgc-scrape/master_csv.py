import csv
from glob import glob

# Clear file contents before writing
# Otherwise creates duplicate rows

file = open('master.csv', 'w+')
file.close()


with open('master.csv', 'a') as master:
    master.write('file, title_column, column_1, column_2, column_3, column_4\n')
    for csv in glob('retrieved_csv/*.csv'):
        csv_name = str(csv)
        csv_file = open(csv, 'r')
        # Skip row head from each csv
        next(csv_file, None)
        for line in csv_file:
            # print('{},{}'.format(csv_name, ','.join([i for i in line.split('\t')])))
            master.write('{},{}'.format(csv_name, ','.join([i for i in line.split('\t')])))
