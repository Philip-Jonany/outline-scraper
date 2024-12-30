import unittest

from outline_scraper import split_by_books

class TestSplitByBooks(unittest.TestCase):
    def test_equals(self):
        # split_by_book tests
        split_by_books_1 = "in the millennial kingdom)-Num. 14:27-30; Phil. 3:12-14: Ten of the twelve men"
        split_by_books_1_answer = [("Num.", " 14:27-30; "), ("Phil.", " 3:12-14: Ten of the twelve men")]
        self.assertEqual(split_by_books_1_answer, split_by_books(split_by_books_1))

        # split_section_by_chapters tests
        # integration test

        # testHasJohnInName = "Title...1 John 4:8-10; 11-13; John 3:1; 14-16; Now, John loved to sing a Song. John also doesn't have a Job. Num. 1:3"
        

if __name__ == '__main__':
    unittest.main()