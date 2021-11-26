import os
import pandas as pd

def check_for_new_file(directory):
    data_directory = directory
    print('Your folder path is"',data_directory,'"')
    before = dict ([(f, None) for f in os.listdir(data_directory)])
    while True:
        after = dict ([(f, None) for f in os.listdir(data_directory)])
        added = [f for f in after if not f in before]
        if added:
            print("Added: ", ", ".join (added))
            path_to_file = data_directory + "/" + added[0]
            print(path_to_file)
            extraction(path_to_file)
            break
        else:
            before = after

def extraction(path_to_file):
    try:
        excel_file = pd.read_excel(path_to_file, engine='openpyxl')
        print(excel_file)
    except Exception as e:
        print(str(e))

    #data_object = 0
    #return data_object


def transformation(data):

    data_transformed = 0
    return data_transformed


def load(data_transformed):
    print("Data has successfully loaded to database.")

check_for_new_file("./DataDirectory")

        
