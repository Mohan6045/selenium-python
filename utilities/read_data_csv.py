import csv


def getCSVData(Filename):
    # creatte  an empty list to store rows
    rows = []
    # open the csv file

    datafile = open(Filename, "r")
    # create a csv reader from csv file
    reader = csv.reader(datafile)
    # sskipthe headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
