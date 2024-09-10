import unittest

import numpy as np
from task import parseDataset


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_Counter(self):
        user_out_put = parseDataset()
        real_answer = np.array([[142, 81, 39, 35],
                               [28, 14, 8, 3],
                               [17, 5, 2, 2],
                               [19, 17, 3, 13],
                               [9, 4, 1, 7],
                               [1, 0, 0, 3],
                               [18, 18, 13, 1],
                               [52, 14, 18, 4],
                               [38, 36, 21, 3],
                               [6, 3, 18, 0],
                               [42, 34, 11, 2],
                               [5, 2, 17, 0]])
        print("your output:", user_out_put)
        self.assertTrue(np.array_equal(user_out_put,real_answer), msg="user output and correct answer is equal")
