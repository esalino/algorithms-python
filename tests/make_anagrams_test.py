import unittest

from maps.make_anagrams import make_anagrams


class TestMakeAnagrams(unittest.TestCase):
    def test_make_anagrams(self):
        result = make_anagrams("cde", "abc")
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
