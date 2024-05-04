import csv
with open('data_file.csv', 'w', newline="") as csvfile:
    # Write the header row if necessary 
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Name', 'Mobile #'])

