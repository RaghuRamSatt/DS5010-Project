from descriptive_statistics import * 
from Probability import *
import csv

# Define a function to calculate the binomial
def calculate_binomial(selection, selectCode):
    n = len(selection)
    k = sum(selectCode)
    p = k/n
    return {'n': n, 'k': k, 'p': p}

def read_csv_file(file_name):
    # Read the data from the CSV file
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
            #print(data)

    # Group the data by condition
    conditions = {}
    for row in data:
        condition = row['condition']
        if condition not in conditions:
            conditions[condition] = []
        conditions[condition].append(row)
        #print(conditions)

    # Calculate the binomial for each condition
    for condition, rows in conditions.items():
        selection = [row['selection'] for row in rows]
        selectCode = [int(row['selectCode']) for row in rows]
        binomial = calculate_binomial(selection, selectCode)
        binomial['condition'] = condition
        print(binomial)

if __name__ == "__main__":
    file = read_csv_file('binomial-data.csv')
    print(file)
