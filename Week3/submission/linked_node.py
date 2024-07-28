class LinkedNode:
    def __init__(self, data=None, next_node=None):
        """
        Create a new LinkedNode with the given data object and next node.

        :param data: data to store in the node
        :param next_node: the next node
        """
        self.data = data
        self.next = next_node

    def get_data(self):
        """
        Get the data stored in the node.

        :return: data in this node.
        """
        return self.data

    def get_next(self):
        """
        Get the next node.

        :return: next node.
        """
        return self.next

    def set_next(self, next_node):
        """
        Set the next node.

        :param next_node: new next node.
        """
        self.next = next_node

    def __str__(self):
        return f"Node containing: {self.data}"
