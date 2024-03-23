class write_demo:
    def __init__(self):
        import os

        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # open a channel/"file handle"
        file = open(file="write_target.txt", mode="a")

        # write something
        file.write("\nHi a new line here")

        # close the channel/"file handle"
        file.close()


write_demo()
