import glob
import os
import shutil

file_path = "c:/Users/Henry/workspace/sdv602-milestone-two-emfriis/data_source/placeholder1.csv"
data_path = os.path.dirname(os.path.abspath(__file__)) + "\data_source"

if glob.glob(data_path + "\{}".format(os.path.basename(file_path))):
    print(file_path)
    
print("$" + file_path)
print("$" + data_path)
print("$" + data_path + "\{}".format(os.path.basename(file_path)))