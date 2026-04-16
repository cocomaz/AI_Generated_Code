def reverse_string(s: str) -> str:
    """
    입력받은 문자열을 역순으로 반환하는 함수입니다.
    
    Args:
        s (str): 뒤집을 대상 문자열
        
    Returns:
        str: 순서가 뒤집힌 문자열
    """
    # 파이썬의 슬라이싱 기능을 사용하여 문자열을 역순으로 생성합니다.
    # [시작:끝:증감값]에서 증감값을 -1로 설정하면 역순으로 정렬됩니다.
    return s[::-1]

# 테스트 코드 (선택 사항)
if __name__ == "__main__":
    test_cases = {
        "hello": "olleh",
        "": "",
        "a": "a",
        "Python": "nohtyP",
        "12345": "54321"
    }
    
    for input_str, expected in test_cases.items():
        result = reverse_string(input_str)
        print(f"Input: '{input_str}' -> Result: '{result}' | {'Success' if result == expected else 'Fail'}")