import unittest

from main.business.energymonitor.digit_splitter import DigitSplitter


class DigitSplitterTest(unittest.TestCase):

    def test_get_nth_digit(self):
        # given
        digit_splitter = DigitSplitter(54137)
        test_cases = [(0,7),(4,5),(2,1),(7,0)]

        for index, expected_digit in test_cases:
            # when
            actual_digit = digit_splitter.get_nth_digit(index)

            #  then
            self.assertEqual(expected_digit, actual_digit)


if __name__ == '__main__':
    unittest.main()
