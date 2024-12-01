import unittest

from outline_scraper import split_by_books
test1 = "in the millennial kingdom)-Num. 14:27-30; Phil. 3:12-14: Ten of the twelve men"
test1_answer = [("Num.", " 14:27-30; "), ("Phil.", " 3:12-14: Ten of the twelve men")]

class TestSplitByBooks(unittest.TestCase):
    def test_split_by_books(self):
        self.assertEqual(test1_answer, split_by_books(test1))

if __name__ == '__main__':
    unittest.main()