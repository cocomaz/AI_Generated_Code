import unittest
from io import StringIO
from unittest.mock import patch
from num_print import print_numbers

class TestNumPrint(unittest.TestCase):
    def test_print_numbers_output(self):
        """
        Test that print_numbers() prints integers from 1 to 34 sequentially.
        """
        # Capture stdout
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_numbers()
            output = fake_out.getvalue().strip().split('\n')
            
            # Expected output: numbers 1 to 34 as strings
            expected_output = [str(i) for i in range(1, 35)]
            
            self.assertEqual(output, expected_output, "The output should be numbers from 1 to 34 sequentially.")

if __name__ == "__main__":
    unittest.main()
