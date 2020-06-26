from collections import defaultdict
import csv


def get_data():
    """
    :return: data from csv and column count
    """
    columns = defaultdict(list)  # each value in each column is appended to a list

    with open('data.csv', encoding="CP1251", newline='', errors='ignore') as csv_in_file:
        reader = csv.DictReader(csv_in_file, delimiter=';')  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k

    return columns
