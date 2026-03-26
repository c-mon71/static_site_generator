import unittest
from title import extract_title

class MyTestCase(unittest.TestCase):
    def test_something(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")  # add assertion here
        title = extract_title("Test \n# Hello")
        self.assertEqual(title, "Hello")
        title = extract_title("Test # Hello")
        self.assertEqual(title, )

if __name__ == '__main__':
    unittest.main()
