
class calculator:
    # def __init__(self):
    #     pass
    
    def add(self, left, right):
        result = left + right
        print(f"{left} + {right} = {result}")
        
    def monkeymath(self, left, right):
        result = left * right
        print(f"{left} + {right} = {result}")
        


calculator = calculator()
calculator.add(left=1,right=2)
calculator.monkeymath(left=1, right=2)