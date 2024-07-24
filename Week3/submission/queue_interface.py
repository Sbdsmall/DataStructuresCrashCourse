from abc import ABC, abstractmethod

class QueueInterface(ABC):
    INITIAL_CAPACITY = 11

    @abstractmethod
    def dequeue(self):
        """
        Dequeue from the front of the queue.
        
        This method should be implemented in O(1) time.
        
        :return: the data from the front of the queue
        :raises: NoSuchElementException if the queue is empty
        """
        pass

    @abstractmethod
    def enqueue(self, data):
        """
        Add the given data to the queue.
        
        This method should be implemented in (if array-backed, amortized) O(1) time.
        
        :param data: the data to add
        :raises: ValueError if data is None
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Return true if this queue contains no elements, false otherwise.
        
        This method should be implemented in O(1) time.
        
        :return: true if the queue is empty; false otherwise
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return the size of the queue.
        
        This method should be implemented in O(1) time.
        
        :return: number of items in the queue
        """
        pass