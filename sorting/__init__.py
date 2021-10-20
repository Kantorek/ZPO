# Pozostaw ten plik pusty, ew. wykorzystaj do własnych testów.

import unittest
import sort


class TestFunctions(unittest.TestCase):

    def test_quicksort(self):
        self.assertListEqual(sort.quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubblesort(self):
        self.assertTupleEqual(sort.bubblesort([1, 2, 3, 4, 5, 6, 7, 8, 9]), ([1, 2, 3, 4, 5, 6, 7, 8, 9], 36))


if __name__ == '__main__':
    unittest.main()