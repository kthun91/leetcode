import unittest
import task3


class TestTask3(unittest.TestCase):

    def test_firstCase(self):
        solution = task3.Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), ["abc", 3])

    def test_secondCase(self):
        solution = task3.Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), ["b", 1])

    def test_thirdCase(self):
        solution = task3.Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), ["wke", 3])


if __name__ == "__main__":
    unittest.main()
