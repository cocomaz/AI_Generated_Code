from utils.string_utils import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh", "테스트 실패: 'hello'를 뒤집어 'olleh'가 되어야 합니다."
    assert reverse_string("") == "", "테스트 실패: 빈 문자열을 뒤집어도 여전히 빈 문자열이어야 합니다."
    assert reverse_string("a") == "a", "테스트 실패: 한 개의 문자로 이루어진 문자열은 그대로 반환되어야 합니다."
    assert reverse_string("12345") == "54321", "테스트 실패: '12345'를 뒤집어 '54321'가 되어야 합니다."
    assert reverse_string("!@#$%") == "%$#@!", "테스트 실패: 특수 문자열 '!@#$%'를 뒤집어 '%$#@!'가 되어야 합니다."
    print("모든 테스트를 통과했습니다.")

test_reverse_string()