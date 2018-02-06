from input import load_file
from time import ctime

def take_data():
    filename = 'test1.xlsx'
    edges = load_file(filename)
    return([{filename: edges}, ctime()])


