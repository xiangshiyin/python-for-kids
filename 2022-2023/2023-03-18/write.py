import os

current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)
sample_file_path = f"{current_file_dir}/sample_write.txt"
print(sample_file_path)

with open(sample_file_path,'w') as file:
    file.write('This is the first line')

# with open(sample_file_path,'w') as file:
#     file.writelines(['This is the first line\n', 'This is the second line'])