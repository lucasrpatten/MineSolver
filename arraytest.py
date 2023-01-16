import unittest
import numpy as np

class TestEasy(unittest.TestCase):

    def test_easy1(self):
        small_game = np.array([["E", "E", "E", "E", "E", 1, "U", "U", "U", "U"],
                           ["E", "E", "E", "E", "E", 1, 2, 4, "U", "U"],
                           [1, 1, 1, "E", "E", "E", "E", 2, "U", "U"],
                           ["U", "U", 1, "E", "E", "E", "E", 1, 1, 1],
                           ["U", 2, 1, "E", "E", "E", "E", "E", "E", "E"],
                           ["U", 1, "E", "E", "E", "E", "E", "E", "E", "E"],
                           ["U", 1, 2, 1, 1, "E", "E", "E", 1, 1],
                           ["U", "U", "U", "U", 1, "E", "E", "E", 1, "U"]])
        should_return = np.array([["E", "E", "E", "E", "E", 1, "X", "X", "U", "U"],
                    ["E", "E", "E", "E", "E", 1, 2, 4, "U", "U"],
                    [1, 1, 1, "E", "E", "E", "E", 2, "X", "S"],
                    ["S", "X", 1, "E", "E", "E", "E", 1, 1, 1],
                    ["X", 2, 1, "E", "E", "E", "E", "E", "E", "E"],
                    ["S", 1, "E", "E", "E", "E", "E", "E", "E", "E"],
                    ["S", 1, 2, 1, 1, "E", "E", "E", 1, 1],
                    ["S", "X", "S", "X", 1, "E", "E", "E", 1, "X"]])
        self.assertEqual(sum([1, 2, 3]), should_return, "Should be 6")

if __name__ == '__main__':
    unittest.main()
