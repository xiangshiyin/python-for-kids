# open a channel/"file handle"
file = open(
    file="/Users/xiangshiyin/Documents/Teaching/python-for-kids/2023-2024/2024-03-16/write_target.txt",
    # mode="w",
    mode="a",
)

# write something
file.write("\nHi a new line here")

# close the channel/"file handle"
file.close()
