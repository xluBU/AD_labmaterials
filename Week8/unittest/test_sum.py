import unittest


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    def testadd(self):
        self.assertEqual(add(4, 5), 9)


if __name__ == '__main__':
    unittest.main()
