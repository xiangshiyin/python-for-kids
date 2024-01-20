class table:
    # constructor method
    def __init__(self, l1, w1, h1):
        self.l = l1
        self.w = w1
        self.h = h1
        self.has_a_flat_top = True
    
    # instance method
    def hold_weight(self, weight):
        print('Holding a weight of {weight} kg')

    def speak(self):
        print('I can speak')
        
t1 = table(l1=1,w1=2,h1=3)
print(t1)
print(t1.l)
print(t1.w)
print(t1.h)
print(t1.speak())
