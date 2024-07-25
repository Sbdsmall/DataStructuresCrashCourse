
from stack_interface import StackInterface


class MyStack(StackInterface):
    def is_empty(self):
        return super().is_empty()
    
    def pop(self):
        return super().pop()
    
    def push(self, data):
        return super().push(data)
    
    def size(self):
        return super().size()
    