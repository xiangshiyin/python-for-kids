
import os

current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)
sample_file_path = f"{current_file_dir}/sample_read.txt"
print(sample_file_path)

with open(sample_file_path,'r') as file:
    print(file.readlines())

# with open('sample_read.txt','r') as file:
#     print(file.readline())