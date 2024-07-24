import unittest
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules

class Test5(unittest.TestCase):
    TIMEOUT = 200

    def test_empty_array_queue(self):
        queue = ArrayQueue()
        with self.assertRaises(NoSuchElementException):
            queue.dequeue()

    def test_null_input_to_array_queue(self):
        queue = ArrayQueue()
        with self.assertRaises(ValueError):
            queue.enqueue(None)

    def test_array_queue(self):
        queue = ArrayQueue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(1)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        backing_array = queue.get_backing_array()
        expected = [None, None, None, 4, 5] + [None] * 6
        self.assertListEqual(expected, backing_array)

        for i in range(5, 14):
            queue.enqueue(i)
            expected[i % 11] = i

        self.assertListEqual(expected, backing_array)

        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)

        queue.enqueue(14)
        queue.enqueue(15)
        queue.enqueue(100)

        expected = [None, None, None, None, None] + [6, 7, 8, 9, 10, 11] + [12, 13, 14, 15, 100] + [None] * 8
        backing_array = queue.get_backing_array()
        self.assertListEqual(expected, backing_array)

        for i in range(12, 23):
            expected[i] = i * 2
            queue.enqueue(i * 2)

        self.assertListEqual(queue.get_backing_array(), expected)
        queue.enqueue(11111)

        self.assertEqual(len(queue.get_backing_array()), 47)

if __name__ == '__main__':
    unittest.main()
