import unittest

from my_module import greet


class TestMyModule(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("PyBuilder"), "Hello, PyBuilder!")


if __name__ == '__main__':
    unittest.main()
