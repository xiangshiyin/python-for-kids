class table:
    def __init__(self, l, w, h):
        self.l = l # attributes
        self.w = w
        self.h = h
        self.has_a_flat_top = True
        
    def hold_weight(self, weight):# method
        print(f'Holding a weight of {weight} kg')

# define a table
t1 = table(l=1, w=2, h=3)
print(f"The table has a length of {t1.l}")
print(f"The table has a width of {t1.w}")
print(f"The table has a height of {t1.h}")
t1.hold_weight(weight=100)

t2 = table(l=2, w=3, h=4)
print(f"The table has a length of {t2.l}")
print(f"The table has a width of {t2.w}")
print(f"The table has a height of {t2.h}")
t2.hold_weight(weight=200)