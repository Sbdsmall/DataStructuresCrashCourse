from linked_node import LinkedNode
from queue_interface import QueueInterface



class MyQueue(QueueInterface):
    def __init__(self, node: 'LinkedNode' = LinkedNode()):
        self.head = node
        self.tail = self.head
        self.size = 0
    def dequeue(self):
        # should remove the item from the top of the queue
        if (self.is_empty()):
             raise ValueError("NoSuchElementException -> Queue is already empty")
        reversePop = self.head.data
        self.head = self.head.next
        self.size -= 1

        return reversePop
    
    def enqueue(self, data):
        if (data == None):
            raise ValueError("data is None")
        queueLooping = self.head

        while(queueLooping != None):
            if (queueLooping.get_next() == None):
                queueLooping.set_next(LinkedNode(data))
                break
            else: 
                queueLooping = queueLooping.get_next()
        
        self.size += 1
    
    def is_empty(self):
        if (self.size() == 0):
            return True
        
        return False
    
    def size(self):
        counter = 0
        sizeQueue = self.head

        while(sizeQueue != None):
            counter += 1
            sizeQueue = sizeQueue.get_next()
        return counter
    

    testQueue = MyQueue(LinkedNode(5))