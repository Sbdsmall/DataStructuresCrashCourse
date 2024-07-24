import unittest
from arrayqueue import ArrayQueue  # Assuming these classes are defined in respective modules
from arraystack import ArrayStack  # Assuming these classes are defined in respective modules
from linkedqueue import LinkedQueue  # Assuming these classes are defined in respective modules
from linkedstack import LinkedStack  # Assuming these classes are defined in respective modules

class Test3(unittest.TestCase):
    TIMEOUT = 200

    def setUp(self):
        self.aqi = ArrayQueue()
        self.asi = ArrayStack()
        self.lqi = LinkedQueue()
        self.lsi = LinkedStack()

    def test_aqi_enqueue(self):
        self.assertTrue(self.aqi.is_empty())
        for i in range(11):
            self.aqi.enqueue(i)
            self.assertEqual(self.aqi.size(), i + 1)
        expected = [i for i in range(11)]
        self.assertListEqual(self.aqi.get_backing_array(), expected)

        for j in range(11):
            self.aqi.enqueue(j)
            self.assertEqual(self.aqi.size(), 12 + j)
        expected2 = [i for i in range(11)] + [i for i in range(11)] + [None]
        self.assertListEqual(self.aqi.get_backing_array(), expected2)

    def test_aqi_dequeue(self):
        self.assertTrue(self.aqi.is_empty())
        for i in range(11):
            self.aqi.enqueue(i)
            self.assertEqual(self.aqi.size(), i + 1)
        self.aqi.enqueue(11)
        self.assertEqual(self.aqi.size(), 12)
        expected = [i for i in range(12)] + [None] * (11 + 1)
        self.assertListEqual(self.aqi.get_backing_array(), expected)

        j = 0
        while not self.aqi.is_empty():
            k = self.aqi.dequeue()
            self.assertEqual(k, expected[j])
            self.assertEqual(self.aqi.size(), 11 - j)
            j += 1

        self.assertListEqual(self.aqi.get_backing_array(), [None] * (QueueInterface.INITIAL_CAPACITY * 2 + 1))

    def test_aqi_circular(self):
        for i in range(11):
            self.aqi.enqueue(i)
            self.assertEqual(self.aqi.size(), i + 1)
        expected = [i for i in range(11)]
        self.assertListEqual(self.aqi.get_backing_array(), expected)
        self.aqi.dequeue()
        self.aqi.dequeue()
        self.assertEqual(self.aqi.size(), 9)
        self.aqi.enqueue(11)
        self.aqi.enqueue(12)

        expected2 = [11, 12] + [i for i in range(2, 11)]
        self.assertListEqual(self.aqi.get_backing_array(), expected2)

        self.assertEqual(self.aqi.dequeue(), 2)
        self.aqi.enqueue(13)
        self.aqi.enqueue(14)
        expected3 = [i for i in range(3, 11)] + [11, 12, 13, 14] + [None] * 11
        self.assertListEqual(self.aqi.get_backing_array(), expected3)

    def test_aqi_enqueue_throws_iae_null_data(self):
        with self.assertRaises(ValueError):
            self.aqi.enqueue(None)

    def test_aqi_dequeue_throws_nsee_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.aqi.dequeue()

    def test_lqi_enqueue(self):
        self.assertTrue(self.lqi.is_empty())
        for i in range(11):
            self.lqi.enqueue(i)
            self.assertEqual(self.lqi.size(), i + 1)

        expected = [i for i in range(11)]
        iter_node = self.lqi.get_head()
        for j in range(self.lqi.size()):
            self.assertEqual(iter_node.get_data(), expected[j])
            iter_node = iter_node.get_next()

    def test_lqi_dequeue(self):
        self.assertTrue(self.lqi.is_empty())
        for i in range(11):
            self.lqi.enqueue(i)
            self.assertEqual(self.lqi.size(), i + 1)

        expected = [i for i in range(11)]
        for j in range(self.lqi.size()):
            self.assertEqual(self.lqi.dequeue(), expected[j])
            self.assertEqual(self.lqi.size(), 10 - j)

        self.assertIsNone(self.lqi.get_head())
        self.assertIsNone(self.lqi.get_tail())
        self.assertEqual(self.lqi.size(), 0)

    def test_lqi_enqueue_throws_iae_null_data(self):
        with self.assertRaises(ValueError):
            self.lqi.enqueue(None)

    def test_lqi_dequeue_throws_nsee_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.lqi.dequeue()

    def test_asi_push(self):
        self.assertTrue(self.asi.is_empty())
        for i in range(11):
            self.asi.push(i)
            self.assertEqual(self.asi.size(), i + 1)

        expected = [i for i in range(11)]
        self.assertListEqual(self.asi.get_backing_array(), expected)

        self.asi.push(11)
        self.assertEqual(self.asi.size(), 12)

        expected2 = expected + [11] + [None] * (11)
        self.assertListEqual(self.asi.get_backing_array(), expected2)

    def test_asi_pop(self):
        self.assertTrue(self.asi.is_empty())
        for i in range(11):
            self.asi.push(i)
            self.assertEqual(self.asi.size(), i + 1)

        expected = [i for i in range(11)]
        self.assertListEqual(self.asi.get_backing_array(), expected)

        for j in range(10, -1, -1):
            self.assertEqual(self.asi.pop(), expected[j])
            self.assertEqual(self.asi.size(), j)

        self.assertListEqual(self.asi.get_backing_array(), [None] * 11)

    def test_asi_push_throws_iae_null_data(self):
        with self.assertRaises(ValueError):
            self.asi.push(None)

    def test_asi_pop_throws_nsee_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.asi.pop()

    def test_lsi_push(self):
        self.assertTrue(self.lsi.is_empty())
        for i in range(11):
            self.lsi.push(i)
            self.assertEqual(self.lsi.size(), i + 1)

        expected = [i for i in range(10, -1, -1)]
        iter_node = self.lsi.get_head()
        for j in range(11):
            self.assertEqual(iter_node.get_data(), expected[j])
            iter_node = iter_node.get_next()

    def test_lsi_pop(self):
        self.assertTrue(self.lsi.is_empty())
        for i in range(11):
            self.lsi.push(i)
            self.assertEqual(self.lsi.size(), i + 1)

        expected = [i for i in range(10, -1, -1)]
        for j in range(11):
            self.assertEqual(self.lsi.pop(), expected[j])
            self.assertEqual(self.lsi.size(), 10 - j)

        self.assertIsNone(self.lsi.get_head())

    def test_lsi_push_throws_iae_null_data(self):
        with self.assertRaises(ValueError):
            self.lsi.push(None)

    def test_lsi_pop_throws_nsee_empty(self):
        with self.assertRaises(NoSuchElementException):
            self.lsi.pop()

if __name__ == '__main__':
    unittest.main()
