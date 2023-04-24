import csv
from descriptive_statistics import *
from Probability import *
import numpy as np



def read_data_file(file_name):
    """Reads a txt file containing a single float number per line and 
    returns a list of integers.
        
    Args:
        file_name (str): Name of the txt file to read from.
    
    Returns:
        list[int]: A list of integers containing the data from the file.
    """
    
    with open(file_name, 'r') as file:
        data_list = [int(line.strip()) for line in file]
    
    return data_list


def read_data_csv(filename):
    # Create a list to store the selectCode values
    select_codes = []
    
    # Read in the CSV file
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract the selectCode value and convert it to an integer
            select_code = int(row['selectCode'])
            
            # Add the selectCode value to the list
            select_codes.append(select_code)
    
    return select_codes
