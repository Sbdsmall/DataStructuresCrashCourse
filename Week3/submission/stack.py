
from stack_interface import StackInterface


class MyStack(StackInterface):
    def is_empty(self):
        if (self.size() > 0): return False
        return True
    
    def pop(self):
        return super().pop()
    
    def push(self, data):
        if (data == None): 
            raise ValueError('param data cannot be None')
        return super().push(data)
    
    def size(self):
        return len(self)
    