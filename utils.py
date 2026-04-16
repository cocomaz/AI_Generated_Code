def find_max(lst):
    """
    리스트 내의 숫자 중 최댓값을 찾아 반환합니다.

    Args:
        lst (list): 정수 또는 실수가 포함된 리스트

    Returns:
        float/int/None: 리스트의 최댓값. 리스트가 비어 있을 경우 None을 반환합니다.
    """
    # 빈 리스트인 경우 None 반환
    if not lst:
        return None
    
    # 내장 함수 max()를 사용하여 최댓값 계산
    return max(lst)

# 테스트 코드 (파일 직접 실행 시 작동)
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 5),          # 양수 리스트
        ([-10, -20, -5, -15], -5),     # 음수 리스트
        ([1.2, 3.9, 2.5, 0.1], 3.9),   # 실수 리스트
        ([10, -10, 0], 10),            # 양수/음수 혼합
        ([7], 7),                      # 단일 요소 리스트
        ([], None),                    # 빈 리스트
    ]

    for i, (input_val, expected) in enumerate(test_cases):
        result = find_max(input_val)
        print(f"Test {i+1}: input={input_val}, result={result}, expected={expected} | {'Pass' if result == expected else 'Fail'}")