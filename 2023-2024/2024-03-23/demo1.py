import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# open a channel/"file handle"
file = open(file="write_target.txt", mode="a")
# file = open(
#     file="/Users/xiangshiyin/Documents/Teaching/python-for-kids/2023-2024/2024-03-23/write_target.txt",
#     mode="a",
# )

# write something
file.write("\nHi a new line here")

# close the channel/"file handle"
file.close()
