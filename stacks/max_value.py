# design a stack data structure that does push, pop and also finds the max value 

# I have to create a variable called min number set to minus infinity,
# and then the append function will add a value to the stack while simulteneously keeping track of the element


from math import inf

class Stack: 
    def __init__(self):
        self.stack = []
        self.max_values = []
        self.max_value = float(-inf)

    def append(self, value): 
        self.stack.append(value)
        if value > self.max_value: 
            self.max_values.append(value)
            self.max_value = value 

    def pop(self): 
        if self.stack[-1] == self.max_value: 
            self.stack.pop()
            self.max_values.pop()
            if self.max_values:
                self.max_value = self.max_values[-1]
            else:
                self.max_value = float(-inf)
        else: 
            self.stack.pop()

    def get_max_value(self):
        return self.max_value



max_stack = Stack()

max_stack.append(8)

print(max_stack.get_max_value())