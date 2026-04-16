def multiply(a, b):
    """
    두 숫자를 곱하는 함수
    
    매개변수:
        a (int | float): 첫 번째 숫자
        b (int | float): 두 번째 숫자
    
    반환값:
        int | float: a와 b를 곱한 결과
    
    예시:
        >>> multiply(2, 3)
        6
        >>> multiply(2.5, 2)
        5.0
    """
    # 입력값 검증: 숫자인지 확인
    if not isinstance(a, (int, float)):
        raise TypeError(f"첫 번째 인자는 숫자여야 합니다. 받은 타입: {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"두 번째 인자는 숫자여야 합니다. 받은 타입: {type(b).__name__}")
    
    # 두 숫자의 곱 반환
    return a * b


if __name__ == "__main__":
    # 간단한 테스트 실행
    print(f"multiply(2, 3) = {multiply(2, 3)}")      # 예상: 6
    print(f"multiply(2.5, 2) = {multiply(2.5, 2)}")  # 예상: 5.0
    print(f"multiply(-3, 4) = {multiply(-3, 4)}")    # 예상: -12
    print(f"multiply(0, 100) = {multiply(0, 100)}")  # 예상: 0