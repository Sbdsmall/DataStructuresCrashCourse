from abc import ABC, abstractmethod

class StackInterface(ABC):
    INITIAL_CAPACITY = 11

    @abstractmethod
    def is_empty(self):
        """
        Return true if this stack contains no elements, false otherwise.
        
        This method should be implemented in O(1) time.
        
        :return: true if the stack is empty; false otherwise
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Pop from the stack.
        
        Removes and returns the top-most element on the stack.
        This method should be implemented in O(1) time.
        
        :return: the data from the top of the stack
        :raises: NoSuchElementException if the stack is empty
        """
        pass

    @abstractmethod
    def push(self, data):
        """
        Push the given data onto the stack.
        
        The given element becomes the top-most element of the stack.
        This method should be implemented in (if array-backed, amortized) O(1) time.
        
        :param data: the data to add
        :raises: ValueError if data is None
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return the size of the stack.
        
        This method should be implemented in O(1) time.
        
        :return: number of items in the stack
        """
        pass
