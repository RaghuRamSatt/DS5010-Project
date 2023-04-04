import csv
from descriptive_statistics import *
import numpy as np
import scipy.stats as stats



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


def read_data_csv(file_name):
    """Reads a CSV file containing a single integer value per row and 
    returns a list of integers.
        
    Args:
        file_name (str): Name of the CSV file to read from.
    
    Returns:
        list[int]: A list of integers containing the data from the file.
    """
    
    with open(file_name, 'r') as file:
        data_list = []
        reader = csv.reader(file)
        for row in reader:
            data_list.append(int(row[0]))
    
    return data_list



