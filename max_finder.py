from typing import List, Union, Optional

def find_max(lst: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """
    리스트 내의 최댓값을 찾아 반환합니다.
    
    Args:
        lst (List[Union[int, float]]): 정수 또는 실수가 포함된 리스트
        
    Returns:
        Optional[Union[int, float]]: 최댓값. 빈 리스트일 경우 None을 반환합니다.
    """
    # 1. 빈 리스트 처리: 리스트가 비어있으면 None 반환
    if not lst:
        return None
    
    # 2. 내장 함수 max()를 사용하여 최댓값 계산
    return max(lst)

def run_tests():
    """
    find_max 함수의 동작을 검증하기 위한 테스트 케이스 실행 함수
    """
    test_cases = [
        {"input": [1, 5, 3], "expected": 5, "desc": "양수 정수 리스트"},
        {"input": [-10, -2, -30], "expected": -2, "desc": "음수 정수 리스트"},
        {"input": [1.5, 2.8, 1.1], "expected": 2.8, "desc": "실수 리스트"},
        {"input": [1, -5, 3.2, -0.5], "expected": 3.2, "desc": "정수 및 실수 혼합 리스트"},
        {"input": [42], "expected": 42, "desc": "단일 요소 리스트"},
        {"input": [], "expected": None, "desc": "빈 리스트"},
    ]

    print("테스트 시작...")
    all_passed = True
    for i, case in enumerate(test_cases):
        result = find_max(case["input"])
        if result == case["expected"]:
            print(f"Case {i+1} [{case['desc']}]: 통과 ✅")
        else:
            print(f"Case {i+1} [{case['desc']}]: 실패 ❌ (기대값: {case['expected']}, 결과값: {result})")
            all_passed = False
    
    if all_passed:
        print("\n모든 테스트 케이스를 성공적으로 통과했습니다!")
    else:
        print("\n일부 테스트 케이스에서 실패가 발생했습니다.")

if __name__ == "__main__":
    run_tests()