import unittest
from sequence_module_22 import get_numbers_forward

class TestSequenceModule22(unittest.TestCase):
    def test_get_numbers_forward(self):
        result = get_numbers_forward()
        expected = list(range(1, 23))
        
        # 1. 정확한 리스트 반환 검증
        self.assertEqual(result, expected, "Forward sequence does not match expected list")
        # 2. 리스트 길이 검증 (22개)
        self.assertEqual(len(result), 22, "Forward sequence length should be 22")
        # 3. 시작 및 끝 값 검증
        self.assertEqual(result[0], 1, "Forward sequence should start with 1")
        self.assertEqual(result[-1], 22, "Forward sequence should end with 22")

if __name__ == "__main__":
    unittest.main()
