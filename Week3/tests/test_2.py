import unittest
from linkedstack import LinkedStack  # Assuming these classes are defined in respective modules
from linkedqueue import LinkedQueue  # Assuming these classes are defined in respective modules
from arraystack import ArrayStack  # Assuming these classes are defined in respective modules
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules

class Test1(unittest.TestCase):
    TIMEOUT = 200

    def test_linked_stack_push(self):
        stack = LinkedStack()
        self.assertEqual(stack.size(), 0)

        stack.push("a")
        stack.push("b")
        stack.push("c")
        stack.push("d")

        self.assertEqual(stack.size(), 4)

        current = stack.get_head()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "d")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "c")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "b")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "a")

    def test_linked_stack_pop(self):
        stack = LinkedStack()
        self.assertEqual(stack.size(), 0)

        stack.push("a")
        stack.push("b")
        stack.push("c")
        stack.push("d")
        self.assertEqual(stack.pop(), "d")

        self.assertEqual(stack.size(), 3)

        current = stack.get_head()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "c")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "b")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "a")

        self.assertIsNone(current.get_next())

    def test_linked_queue_enqueue(self):
        queue = LinkedQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue("a")
        queue.enqueue("b")
        queue.enqueue("c")
        queue.enqueue("d")

        self.assertEqual(queue.size(), 4)

        current = queue.get_head()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "a")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "b")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "c")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "d")

    def test_linked_queue_dequeue(self):
        queue = LinkedQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue("a")
        queue.enqueue("b")
        queue.enqueue("c")
        queue.enqueue("d")

        self.assertEqual(queue.size(), 4)
        self.assertEqual(queue.dequeue(), "a")
        self.assertEqual(queue.size(), 3)
        current = queue.get_head()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "b")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "c")

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), "d")

        self.assertIsNone(current.get_next())

    def test_array_stack_resize(self):
        aStack = ArrayStack()
        self.assertEqual(aStack.size(), 0)
        for i in range(1, 13):
            aStack.push(i)
        self.assertEqual(aStack.size(), 12)
        self.assertEqual(len(aStack.get_backing_array()), 23)

        backing_array = aStack.get_backing_array()
        expected = [i for i in range(1, 13)] + [None] * 11
        self.assertListEqual(expected, backing_array)

    def test_array_stack_resize_pop(self):
        aStack = ArrayStack()
        self.assertEqual(aStack.size(), 0)
        for i in range(1, 13):
            aStack.push(i)
        self.assertEqual(aStack.size(), 12)
        self.assertEqual(len(aStack.get_backing_array()), 23)
        self.assertEqual(aStack.pop(), 12)
        self.assertEqual(aStack.size(), 11)

        backing_array = aStack.get_backing_array()
        expected = [i for i in range(1, 12)] + [None] * 12
        self.assertListEqual(expected, backing_array)

    def test_pop_one(self):
        aStack = ArrayStack()
        aStack.push(1)
        self.assertEqual(aStack.size(), 1)
        self.assertEqual(aStack.pop(), 1)
        self.assertEqual(aStack.size(), 0)

        stack = LinkedStack()
        stack.push("a")
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), "a")
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.get_head())

    def test_dequeue_one(self):
        aQueue = ArrayQueue()
        aQueue.enqueue(1)
        self.assertEqual(aQueue.size(), 1)
        self.assertEqual(aQueue.dequeue(), 1)
        self.assertEqual(aQueue.size(), 0)

        queue = LinkedQueue()
        queue.enqueue("a")
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), "a")
        self.assertEqual(queue.size(), 0)
        self.assertIsNone(queue.get_head())
        self.assertIsNone(queue.get_tail())

    def test_queue_stack_resize(self):
        aQueue = ArrayQueue()
        for i in range(1, 13):
            aQueue.enqueue(i)
        self.assertEqual(aQueue.size(), 12)
        self.assertEqual(len(aQueue.get_backing_array()), 23)

        expected = [i for i in range(1, 13)] + [None] * 11
        self.assertListEqual(expected, aQueue.get_backing_array())

    def test_queue_stack_resize_dequeue(self):
        aQueue = ArrayQueue()
        for i in range(1, 13):
            aQueue.enqueue(i)
        self.assertEqual(aQueue.size(), 12)
        self.assertEqual(aQueue.dequeue(), 1)
        self.assertEqual(aQueue.size(), 11)
        self.assertEqual(len(aQueue.get_backing_array()), 23)

        expected = [None] + [i for i in range(2, 13)] + [None] * 11
        self.assertListEqual(expected, aQueue.get_backing_array())

    def test_shifting_front_and_back(self):
        aQueue = ArrayQueue()
        for i in range(1, 4):
            aQueue.enqueue(i)
        self.assertEqual(aQueue.size(), 3)
        self.assertEqual(aQueue.dequeue(), 1)
