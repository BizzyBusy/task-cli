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
            
        single_args = ["list", "add", "update", "delete", "mark-done", "mark-in-progress", "hello", " hello", "", " ", "1"]

        for arg in single_args:
                self.assertEqual(helper.isValidOp(["", arg]), arg == "list", f'The single argument "{arg}" is incorrectly passed as valid.')

    def test_addValid(self):
        """
        Testing that isValidOp correctly detects a valid add operation.
        """

        bank = ["1", "task", "", " ", "hello ", " hello", " hello ", "@", "hello    world", "list"]

        for second_arg in bank:
            self.assertTrue(helper.isValidOp(["", "add", second_arg]), f'The second argument "{second_arg}" led to the add operation incorrectly failing, despite being valid in length.')

        input = ["", "add", "", "  "]
        self.assertFalse(helper.isValidOp(input), 'Invalid input length.')


    def test_deleteMarkValid(self):
        """
        Testing that isValidOp correctly detects valid delete and mark operations.
        """

        op_bank = ["delete", "mark-done", "mark-in-progress"]

        for op in op_bank:
            self.assertTrue(helper.isValidOp(["", op, "1"]), f'Following argument must be a number.')

            self.assertFalse(helper.isValidOp(["", op, "1", " ", " "]), f'"{op}" operation takes only one additional argument. ')


        bank = ["task", "", " ", "hello ", " hello", " hello ", "@", "hello    world" "list"]
        for second_arg in bank:
            for op in op_bank:
                self.assertFalse(helper.isValidOp(["", op, second_arg]), "Following argument must be a number.")
        

    def test_updateValid(self):
        """
        Testing that isValidOp correctly detects a valid update operation.
        """

        input = ["", "update", "1"]
        self.assertFalse(helper.isValidOp(input), 'Two arguments must follow the "update" argument.')

        bank = ["task", "", " ", "hello ", " hello", " hello ", "@", "hello    world", "list"]
        for second_arg in bank:
            self.assertFalse(helper.isValidOp(["", "update", second_arg, second_arg]), "Second argument must be a number.")

        bank.append("1")
        for second_arg in bank:
            self.assertTrue(helper.isValidOp(["", "update", "1", second_arg]), "Second argument must be a number, and third argument can be anything.")

        self.assertFalse(helper.isValidOp(["", "update", "1", " hi ", " "]), '"update" operation takes exactly 2 additional arguments.')


    def test_listValid(self):
        """
        Testing that isValidOp correctly detects valid list operations.
        """

        bank = ["task", "", " ", "hello ", " hello", " hello ", "@", "hello    world", "list", "1"]
        for second_arg in bank:
            self.assertFalse(helper.isValidOp(["", "list", second_arg]), 'If an argument after "list" is entered, it must be one of the following: "done" "todo", "in-progress.')

        second_args = ["done", "todo", "in-progress"]

        for arg in second_args:
            self.assertTrue(helper.isValidOp(["", "list", arg]), 'If an argument after "list" is entered, it must be one of the following: "done" "todo", "in-progress.')

            self.assertFalse(helper.isValidOp(["", "list", arg, "a"]), '"list" operation takes exactly 1 optional argument.')

        
        




if __name__ == '__main__':
    unittest.main()
