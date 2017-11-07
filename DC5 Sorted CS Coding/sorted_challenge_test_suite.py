import cProfile, pstats
import unittest
from sorted_challenge import read_input, clean_symbols, separate_ints_words, sort_lists, reassemble_list


class SortingTestCase(unittest.TestCase):
    """Tests for `sorted_challenge.py`."""

    def test_read_input(self):
        """Are files read in correctly?"""
        self.assertEqual(read_input('test_input1.txt'),
                         ['eighty', '6%', 'lake', 'chal-lenge', '4,,0', 'favorite', '3'])

        self.assertEqual(read_input('test_input2.txt'),
                         [''])

        self.assertEqual(read_input('test_input3.txt'),
                         ['8*', '90', '42', '7', '1-2'])


    def test_clean_symbols(self):
        """Are all non-alphanumeric characters removed?"""
        self.assertEqual(clean_symbols(['6%', 'chal-lenge', '4,,0']),
                                       ['6', 'challenge', '40'])

        self.assertEqual(clean_symbols(['***^5', '"kipper"']),
                                       ['5', 'kipper'])


    def test_separate_ints_words(self):
        """Are integers and words put into separate lists correctly, with original positions recorded?"""
        self.assertEqual(separate_ints_words(['eighty', '6', 'lake', 'challenge', '40', 'favorite', '3']),
                         ([6, 40, 3], ['eighty', 'lake', 'challenge', 'favorite'], [1, 0, 1, 1, 0, 1, 0]))


    def test_sort_lists(self):
        """Are both lists sorted correctly?"""
        self.assertEqual(sort_lists([6, 40, 3], ['eighty', 'lake', 'challenge', 'favorite']),
                         ([40, 6, 3], ['lake', 'favorite', 'eighty', 'challenge']))


    def test_reassemble_list(self):
        """Are lists put back together correctly?"""
        self.assertEqual(reassemble_list([40, 6, 3], ['lake', 'favorite', 'eighty', 'challenge'],
                                         [1, 0, 1, 1, 0, 1, 0]),
                         ['challenge', 3, 'eighty', 'favorite', 6, 'lake', 40])


def profile_script():
    cProfile.run('sorted_challenge.main("test_input1.txt")')
    #p = pstats.Stats('restats')
    #p.strip_dirs().sort_stats(-1).print_stats()


if __name__ == '__main__':
    unittest.main()
