import unittest

from common import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        self.assertEqual(hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
