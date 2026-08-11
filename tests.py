import unittest
import helper

class TestCheckerMethod(unittest.TestCase):
    """
    Tests the correctness of the helper function isValidOp.
    """

    def test_noArgs(self):
        """
        Testing that isValidOp correctly detects when no arguments are provided."""
        
        input = [""]

        res = helper.isValidOp(input)

        self.assertFalse(res, "An input was falsely detected.")


if __name__ == '__main__':
    unittest.main()

        