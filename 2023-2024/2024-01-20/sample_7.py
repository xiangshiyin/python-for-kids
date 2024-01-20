class value:
    def __init__(self, v):
        self.v = v
    
    def __add__(self, other):
        result = self.v + other.v
        print(f"The result is {self.v}")
        return value(v = result)
    
    def __sub__(self, other):
        pass

    def __mult__(self, other):
        pass

    def __div__(self, other):
        pass

v1 = value(v = 1)
v2 = value(v = 2)
v3 = v1 + v2
print(type(v3))
print(v3)
print(v3.v)

