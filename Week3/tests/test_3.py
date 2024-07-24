import unittest
from arraystack import ArrayStack  # Assuming these classes are defined in respective modules
from linkedstack import LinkedStack  # Assuming these classes are defined in respective modules
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules
from linkedqueue import LinkedQueue  # Assuming these classes are defined in respective modules

class Test2(unittest.TestCase):
    TIMEOUT = 200

    def setUp(self):
        self.arrayStack = ArrayStack()
        self.linkedStack = LinkedStack()
        self.arrayQueue = ArrayQueue()
        self.linkedQueue = LinkedQueue()

    def test_array_stack(self):
        self.arrayStack.push("1a")
        self.arrayStack.push("2a")
        self.arrayStack.push("3a")
        self.arrayStack.push("4a")
        self.assertFalse(self.arrayStack.is_empty())
        self.assertEqual(self.arrayStack.size(), 4)

        self.assertEqual(self.arrayStack.pop(), "4a")
        self.assertEqual(self.arrayStack.size(), 3)
        self.assertEqual(self.arrayStack.pop(), "3a")
        self.assertEqual(self.arrayStack.size(), 2)
        self.assertEqual(self.arrayStack.pop(), "2a")
        self.assertEqual(self.arrayStack.size(), 1)
        self.assertEqual(self.arrayStack.pop(), "1a")
        self.assertEqual(self.arrayStack.size(), 0)
        self.assertTrue(self.arrayStack.is_empty())

    def test_array_stack_grow_array(self):
        for i in range(ArrayStack.INITIAL_CAPACITY):
            self.assertEqual(self.arrayStack.size(), i)
            self.arrayStack.push(f"{i}a")
        self.arrayStack.push("11a")
        self.assertEqual(self.arrayStack.size(), 12)

        arr = [f"{i}a" for i in range(ArrayStack.INITIAL_CAPACITY + 1)] + [None] * (ArrayStack.INITIAL_CAPACITY + 1)
        self.assertListEqual(self.arrayStack.get_backing_array(), arr)
        self.assertEqual(self.arrayStack.pop(), "11a")
        self.assertEqual(self.arrayStack.size(), 11)
        arr[11] = None
        self.assertListEqual(self.arrayStack.get_backing_array(), arr)

    def test_array_stack_time(self):
        self.assertEqual(self.arrayStack.size(), 0)
        self.assertTrue(self.arrayStack.is_empty())

        for i in range(100000):
            self.assertEqual(self.arrayStack.size(), i)
            self.arrayStack.push(f"{i}a")

        for i in range(100000 - 1, -1, -1):
            self.assertEqual(self.arrayStack.pop(), f"{i}a")
            self.assertEqual(self.arrayStack.size(), i)

    def test_array_stack_push_null(self):
        with self.assertRaises(ValueError):
            self.arrayStack.push(None)

    def test_array_stack_pop_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.arrayStack.pop()

    def test_linked_stack(self):
        self.assertEqual(self.linkedStack.size(), 0)
        self.assertIsNone(self.linkedStack.get_head())

        self.linkedStack.push("1a")
        self.assertEqual(self.linkedStack.size(), 1)
        self.assertEqual(self.linkedStack.get_head().get_data(), "1a")

        self.linkedStack.push("2a")
        self.assertEqual(self.linkedStack.size(), 2)
        self.assertEqual(self.linkedStack.get_head().get_data(), "2a")

        self.linkedStack.push("3a")
        self.assertEqual(self.linkedStack.size(), 3)
        self.assertEqual(self.linkedStack.get_head().get_data(), "3a")

        self.linkedStack.push("4a")
        self.assertEqual(self.linkedStack.size(), 4)
        self.assertEqual(self.linkedStack.get_head().get_data(), "4a")

        self.assertFalse(self.linkedStack.is_empty())

        self.assertEqual(self.linkedStack.pop(), "4a")
        self.assertEqual(self.linkedStack.size(), 3)
        self.assertEqual(self.linkedStack.get_head().get_data(), "3a")

        self.assertEqual(self.linkedStack.pop(), "3a")
        self.assertEqual(self.linkedStack.size(), 2)
        self.assertEqual(self.linkedStack.get_head().get_data(), "2a")

        self.assertEqual(self.linkedStack.pop(), "2a")
        self.assertEqual(self.linkedStack.size(), 1)
        self.assertEqual(self.linkedStack.get_head().get_data(), "1a")

        self.assertEqual(self.linkedStack.pop(), "1a")
        self.assertEqual(self.linkedStack.size(), 0)
        self.assertIsNone(self.linkedStack.get_head())
        self.assertTrue(self.linkedStack.is_empty())

    def test_linked_stack_time(self):
        self.assertEqual(self.linkedStack.size(), 0)
        self.assertIsNone(self.linkedStack.get_head())

        for i in range(100000):
            self.linkedStack.push(f"{i}a")
            self.assertEqual(self.linkedStack.get_head().get_data(), f"{i}a")
            self.assertEqual(self.linkedStack.size(), i + 1)

        for i in range(100000 - 1, -1, -1):
            self.assertEqual(self.linkedStack.pop(), f"{i}a")
            self.assertEqual(self.linkedStack.size(), i)

        self.assertIsNone(self.linkedStack.get_head())
        self.assertTrue(self.linkedStack.is_empty())
        self.assertEqual(self.linkedStack.size(), 0)

    def test_linked_stack_push_null(self):
        with self.assertRaises(ValueError):
            self.linkedStack.push(None)

    def test_linked_stack_pop_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.linkedStack.pop()

    def test_array_queue(self):
        self.assertTrue(self.arrayQueue.is_empty())
        self.assertEqual(self.arrayQueue.size(), 0)
        self.assertListEqual(self.arrayQueue.get_backing_array(), [None] * ArrayQueue.INITIAL_CAPACITY)

        self.arrayQueue.enqueue("1a")
        self.assertEqual(self.arrayQueue.size(), 1)

        self.arrayQueue.enqueue("2a")
        self.assertEqual(self.arrayQueue.size(), 2)

        self.arrayQueue.enqueue("3a")
        self.assertEqual(self.arrayQueue.size(), 3)

        self.arrayQueue.enqueue("4a")
        self.assertEqual(self.arrayQueue.size(), 4)

        self.assertFalse(self.arrayQueue.is_empty())

        self.assertEqual(self.arrayQueue.dequeue(), "1a")
        self.assertEqual(self.arrayQueue.size(), 3)

        self.assertEqual(self.arrayQueue.dequeue(), "2a")
        self.assertEqual(self.arrayQueue.size(), 2)

        self.assertEqual(self.arrayQueue.dequeue(), "3a")
        self.assertEqual(self.arrayQueue.size(), 1)

        self.assertEqual(self.arrayQueue.dequeue(), "4a")
        self.assertEqual(self.arrayQueue.size(), 0)
        self.assertTrue(self.arrayQueue.is_empty())

    def test_array_queue_grow_array(self):
        self.assertEqual(self.arrayQueue.size(), 0)
        self.assertTrue(self.arrayQueue.is_empty())
        arr = [None] * (QueueInterface.INITIAL_CAPACITY * 2 + 1)
        for i in range(23):
            self.assertEqual(self.arrayQueue.size(), i)
            self.arrayQueue.enqueue(f"{i}a")
            arr[i] = f"{i}a"
        self.assertEqual(self.arrayQueue.size(), 23)
        self.assertListEqual(self.arrayQueue.get_backing_array(), arr)

        self.assertEqual(self.arrayQueue.dequeue(), "0a")
        arr[0] = None
        self.assertListEqual(self.arrayQueue.get_backing_array(), arr)

        for i in range(1, 23):
            self.assertEqual(self.arrayQueue.dequeue(), f"{i}a")
        self.assertTrue(self.arrayQueue.is_empty())

        for i in range(23):
            self.assertEqual(self.arrayQueue.size(), i)
            self.arrayQueue.enqueue(f"{i}a")
            arr[i] = f"{i}a"
        self.assertEqual(len(self.arrayQueue.get_backing_array()), 23)
        self.arrayQueue.enqueue("23a")
        self.assertEqual(len(self.arrayQueue.get_backing_array()), 23 * 2 + 1)

    def test_array_queue_cycle(self):
        for i in range(10):
            self.arrayQueue.enqueue(f"{i}a")
        self.assertEqual(self.arrayQueue.size(), 10)
        for i in range(10, 100000):
            self.arrayQueue.enqueue(f"{i}a")
            self.assertEqual(self.arrayQueue.dequeue(), f"{i - 10}a")
        self.assertEqual(self.arrayQueue.size(), 10)
        self.assertEqual(len(self.arrayQueue.get_backing_array()), QueueInterface.INITIAL_CAPACITY)
        self.assertIsNone(self.arrayQueue.get_backing_array()[10])

    def test_array_queue_dequeue_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.arrayQueue.dequeue()

    def test_array_queue_enqueue_null(self):
        with self.assertRaises(ValueError):
            self.arrayQueue.enqueue(None)

    def test_linked_queue(self):
        self.assertEqual(self.linkedQueue.size(), 0)
        self.assertTrue(self.linkedQueue.is_empty())
        self.assertIsNone(self.linkedQueue.get_head())
        self.assertIsNone(self.linkedQueue.get_tail())

        self.linkedQueue.enqueue("1a")
        self.assertEqual(self.linkedQueue.size(), 1)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "1a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "1a")

        self.linkedQueue.enqueue("2a")
        self.assertEqual(self.linkedQueue.size(), 2)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "1a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "2a")

        self.linkedQueue.enqueue("3a")
        self.assertEqual(self.linkedQueue.size(), 3)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "1a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "3a")

        self.linkedQueue.enqueue("4a")
        self.assertEqual(self.linkedQueue.size(), 4)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "1a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "4a")

        self.assertFalse(self.linkedQueue.is_empty())

        self.assertEqual(self.linkedQueue.dequeue(), "1a")
        self.assertEqual(self.linkedQueue.size(), 3)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "2a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "4a")

        self.assertEqual(self.linkedQueue.dequeue(), "2a")
        self.assertEqual(self.linkedQueue.size(), 2)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "3a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "4a")

        self.assertEqual(self.linkedQueue.dequeue(), "3a")
        self.assertEqual(self.linkedQueue.size(), 1)
        self.assertEqual(self.linkedQueue.get_head().get_data(), "4a")
        self.assertEqual(self.linkedQueue.get_tail().get_data(), "4a")

        self.assertEqual(self.linkedQueue.dequeue(), "4a")
        self.assertEqual(self.linkedQueue.size(), 0)
        self.assertIsNone(self.linkedQueue.get_head())
        self.assertIsNone(self.linkedQueue.get_tail())
        self.assertTrue(self.linkedQueue.is_empty())

    def test_linked_queue_time(self):
        self.assertEqual(self.linkedQueue.size(), 0)
        self.assertTrue(self.linkedQueue.is_empty())
        self.assertIsNone(self.linkedQueue.get_head())
        self.assertIsNone(self.linkedQueue.get_tail())

        self.linkedQueue.enqueue("0a")
        for i in range(1, 100000):
            self.assertEqual(self.linkedQueue.size(), i)
            self.linkedQueue.enqueue(f"{i}a")
            self.assertEqual(self.linkedQueue.get_head().get_data(), "0a")
            self.assertEqual(self.linkedQueue.get_tail().get_data(), f"{i}a")

        for i in range(100000):
            self.assertEqual(self.linkedQueue.get_head().get_data(), f"{i}a")
            self.assertEqual(self.linkedQueue.get_tail().get_data(), "99999a")
            self.assertEqual(self.linkedQueue.dequeue(), f"{i}a")

        self.assertEqual(self.linkedQueue.size(), 0)
        self.assertTrue(self.linkedQueue.is_empty())
        self.assertIsNone(self.linkedQueue.get_head())
        self.assertIsNone(self.linkedQueue.get_tail())

    def test_linked_queue_dequeue_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.linkedQueue.dequeue()

    def test_linked_queue_enqueue_null(self):
        with self.assertRaises(ValueError):
            self.linkedQueue.enqueue(None)

if __name__ == '__main__':
    unittest.main()
