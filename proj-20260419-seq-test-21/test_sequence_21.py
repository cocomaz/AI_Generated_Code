import unittest
from sequence_module_21 import get_numbers_forward, get_numbers_backward

class TestSequenceModule21(unittest.TestCase):
    def test_get_numbers_forward(self):
        result = get_numbers_forward()
        expected = list(range(1, 22))
        
        # 1. 정확한 리스트 반환 검증
        self.assertEqual(result, expected, "Forward sequence does not match expected list")
        # 2. 리스트 길이 검증 (21개)
        self.assertEqual(len(result), 21, "Forward sequence length should be 21")
        # 3. 시작 및 끝 값 검증
        self.assertEqual(result[0], 1, "Forward sequence should start with 1")
        self.assertEqual(result[-1], 21, "Forward sequence should end with 21")

    def test_get_numbers_backward(self):
        result = get_numbers_backward()
        expected = list(range(21, 0, -1))
        
        # 1. 정확한 리스트 반환 검증
        self.assertEqual(result, expected, "Backward sequence does not match expected list")
        # 2. 리스트 길이 검증 (21개)
        self.assertEqual(len(result), 21, "Backward sequence length should be 21")
        # 3. 시작 및 끝 값 검증
        self.assertEqual(result[0], 21, "Backward sequence should start with 21")
        self.assertEqual(result[-1], 1, "Backward sequence should end with 1")

if __name__ == "__main__":
    unittest.main()
