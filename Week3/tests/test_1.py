import unittest
from arraystack import ArrayStack  # Assuming these classes are defined in respective modules
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules

class TestStacksQueuesStudent(unittest.TestCase):
    TIMEOUT = 200

    def test_array_stack_push(self):
        stack = ArrayStack()
        self.assertEqual(stack.size(), 0)

        stack.push(34)
        stack.push(29)
        stack.push(48)
        stack.push(59)

        self.assertEqual(stack.size(), 4)

        backing_array = stack.get_backing_array()
        expected = [None] * 11
        expected[0] = 34
        expected[1] = 29
        expected[2] = 48
        expected[3] = 59

        self.assertListEqual(expected, backing_array)

    def test_array_stack_pop(self):
        stack = ArrayStack()
        self.assertEqual(stack.size(), 0)

        stack.push(34)
        stack.push(29)
        stack.push(48)
        stack.push(59)
        self.assertEqual(stack.pop(), 59)

        self.assertEqual(stack.size(), 3)

        backing_array = stack.get_backing_array()
        expected = [None] * 11
        expected[0] = 34
        expected[1] = 29
        expected[2] = 48

        self.assertListEqual(expected, backing_array)

    def test_array_queue_enqueue(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)
        queue.enqueue(59)

        self.assertEqual(queue.size(), 4)

        backing_array = queue.get_backing_array()
        expected = [None] * 11
        expected[0] = 34
        expected[1] = 29
        expected[2] = 48
        expected[3] = 59

        self.assertListEqual(expected, backing_array)

    def test_array_queue_dequeue(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)
        queue.enqueue(59)
        self.assertEqual(queue.dequeue(), 34)

        self.assertEqual(queue.size(), 3)

        backing_array = queue.get_backing_array()
        expected = [None] * 11
        expected[1] = 29
        expected[2] = 48
        expected[3] = 59

        self.assertListEqual(expected, backing_array)

if __name__ == '__main__':
    unittest.main()