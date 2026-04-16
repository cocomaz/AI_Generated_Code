from typing import List, Optional, Union

def find_max(lst: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """
    리스트 내의 숫자 중 최댓값을 찾아 반환합니다.
    
    Args:
        lst (List[Union[int, float]]): 정수 또는 실수로 구성된 숫자 리스트
        
    Returns:
        Optional[Union[int, float]]: 리스트의 최댓값. 리스트가 비어 있는 경우 None을 반환합니다.
    """
    # 리스트가 비어 있는지 확인 (빈 리스트는 False로 평가됨)
    if not lst:
        return None
    
    # Python 내장 함수 max()를 사용하여 최댓값 반환
    return max(lst)

# 테스트 코드 (검증용)
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 5),           # 양수 리스트
        ([-1, -2, -3, -4], -1),         # 음수 리스트
        ([1.5, 2.8, 0.4, 2.7], 2.8),    # 실수 리스트
        ([10, -5, 3.14, 0], 10),        # 혼합 리스트
        ([42], 42),                     # 단일 요소 리스트
        ([], None),                      # 빈 리스트
    ]

    for i, (input_val, expected) in enumerate(test_cases):
        result = find_max(input_val)
        assert result == expected, f"Test {i} failed: input={input_val}, expected={expected}, got={result}"
        print(f"Test {i} passed: {input_val} -> {result}")