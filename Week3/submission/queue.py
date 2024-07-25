from queue_interface import QueueInterface


class MyQueue(QueueInterface):
    def dequeue(self):
        return super().dequeue()
    
    def enqueue(self, data):
        return super().enqueue(data)
    
    def is_empty(self):
        return super().is_empty()
    
    def size(self):
        return super().size()