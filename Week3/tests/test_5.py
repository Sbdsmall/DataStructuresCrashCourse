import unittest
from arraystack import ArrayStack  # Assuming these classes are defined in respective modules
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules
from linkedstack import LinkedStack  # Assuming these classes are defined in respective modules
from linkedqueue import LinkedQueue  # Assuming these classes are defined in respective modules

class Test4(unittest.TestCase):
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

    def test_array_stack_pop_empty(self):
        stack = ArrayStack()
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(NoSuchElementException):
            stack.pop()

    def test_array_stack_pop_one_element(self):
        stack = ArrayStack()
        self.assertEqual(stack.size(), 0)

        stack.push(34)
        backing_array = stack.get_backing_array()
        expected = [None] * 11
        expected[0] = 34
        self.assertListEqual(expected, backing_array)

        self.assertEqual(stack.pop(), 34)
        self.assertEqual(stack.size(), 0)

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

    def test_array_queue_enqueue_circular(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        for _ in range(8):
            queue.enqueue(59)
        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)

        self.assertEqual(queue.size(), 11)

        backing_array = queue.get_backing_array()
        expected = [34, 29, 48] + [59] * 8
        self.assertListEqual(expected, backing_array)

        self.assertEqual(queue.dequeue(), 34)
        queue.enqueue(0)

        expected[0] = 0
        self.assertListEqual(expected, backing_array)

    def test_array_queue_dequeue_circular(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        for _ in range(8):
            queue.enqueue(59)
        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)

        self.assertEqual(queue.size(), 11)

        backing_array = queue.get_backing_array()
        expected = [34, 29, 48] + [59] * 8
        self.assertListEqual(expected, backing_array)

        self.assertEqual(queue.dequeue(), 34)
        queue.enqueue(0)

        expected[0] = 0
        self.assertListEqual(expected, backing_array)
        queue.dequeue()

        queue.enqueue(10)
        for _ in range(8):
            queue.dequeue()
        queue.dequeue()

        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(queue.dequeue(), 10)

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
        expected = [None, 29, 48, 59] + [None] * 7
        self.assertListEqual(expected, backing_array)

    def test_linked_queue_enqueue(self):
        queue = LinkedQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(18)
        queue.enqueue(27)
        current = queue.get_head()

        self.assertEqual(current.get_data(), 18)
        current = current.get_next()
        self.assertEqual(current.get_data(), 27)

    def test_linked_queue_dequeue(self):
        queue = LinkedQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(18)
        queue.enqueue(27)
        current = queue.get_head()

        self.assertEqual(current.get_data(), 18)
        current = current.get_next()
        self.assertEqual(current.get_data(), 27)

        self.assertEqual(queue.dequeue(), 18)
        self.assertEqual(queue.dequeue(), 27)

    def test_linked_queue_is_empty(self):
        queue = LinkedQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(18)
        queue.enqueue(27)
        current = queue.get_head()

        self.assertEqual(current.get_data(), 18)
        current = current.get_next()
        self.assertEqual(current.get_data(), 27)

        self.assertEqual(queue.dequeue(), 18)
        self.assertEqual(queue.dequeue(), 27)

        self.assertTrue(queue.is_empty())

    def test_linked_stack_enqueue_dequeue_is_empty(self):
        stack = LinkedStack()
        self.assertEqual(stack.size(), 0)

        stack.push(18)
        stack.push(27)
        current = stack.get_head()

        self.assertEqual(current.get_data(), 27)
        current = current.get_next()
        self.assertEqual(current.get_data(), 18)

        self.assertEqual(stack.pop(), 27)
        self.assertEqual(stack.pop(), 18)

        self.assertTrue(stack.is_empty())

    def test_array_queue_enqueue_doubling_no_circle(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        for _ in range(8):
            queue.enqueue(59)
        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)

        self.assertEqual(queue.size(), 11)
        queue.enqueue(37)
        self.assertEqual(len(queue.get_backing_array()), 23)

    def test_array_queue_enqueue_doubling_circular(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        for _ in range(8):
            queue.enqueue(59)
        queue.enqueue(34)
        queue.enqueue(29)
        queue.enqueue(48)

        self.assertEqual(queue.size(), 11)

        backing_array = queue.get_backing_array()
        expected = [34, 29, 48] + [59] * 8
        self.assertListEqual(expected, backing_array)

        self.assertEqual(queue.dequeue(), 34)
        queue.enqueue(0)

        expected[0] = 0
        self.assertListEqual(expected, backing_array)
        queue.enqueue(69)
        self.assertEqual(len(queue.get_backing_array()), 23)
        expected = [29, 48, 59] + [59] * 6 + [0, 69] + [None] * 11
        self.assertListEqual(queue.get_backing_array(), expected)

if __name__ == '__main__':
    unittest.main()
