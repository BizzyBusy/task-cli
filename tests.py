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

    def test_singleArg(self):
        """
        Testing that isValidOp correctly detects the "list" operation as the only valid single argument.
        """
            
        single_args = ["list", "add", "update", "delete", "mark-done", "mark-in-progress"]

        for arg in single_args:
                self.assertEqual(helper.isValidOp(["", arg]), arg == "list", f'The single argument "{arg}" is incorrectly passed as valid.')

    #TODO: COMPLETE THIS FUNCTION BEFORE MOVING ON TO FUTURE TESTCASES
    def test_addValid(self):
        """
        Testing that isValidOp correctly detects a valid add operation.
        """

        bank = ["1", "task", "", " ", "hello ", " hello", " hello ", "@", "hello    world"]

        for second_arg in bank:
            self.assertTrue(helper.isValidOp(["", "add", second_arg]), f'The second argument "{second_arg}" led to the add operation incorrectly failing, despite being valid in length.')


if __name__ == '__main__':
    unittest.main()

        