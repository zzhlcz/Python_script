import unittest

class SearchTests(unittest.TestCase):

    def print_commnon_part(self):
        print("common part!")

    def test_case_01(self):
        self.print_commnon_part()
        print("test_case_01")

    def test_case_02(self):
        self.print_commnon_part()
        print("test_case_02")

    def test_case_03(self):
        self.print_commnon_part()
        print("test_case_03")


if __name__ == '__main__':
    unittest.main(verbosity=2)