
import random

def flip(trials):
    head = 0 
    tail = 0
    for i in range(trials):
        result = random.randint(0,1)
        if result == 1:
            head += 1
        else:
            tail += 1
    # print(result)
    print(f"""
        Number of times with head: {head}
        Number of times with tail: {tail}
          """)

# flip(trials=100)
flip(1000000)
