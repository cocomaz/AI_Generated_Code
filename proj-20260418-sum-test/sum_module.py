def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        float/int: The sum of the numbers, or 0 if the list is empty.
    """
    if not numbers:
        return 0
    
    return sum(numbers)

if __name__ == "__main__":
    # Test cases for verification
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([10, -20, 30], 20),
        ([1.5, 2.5, 3.0], 7.0),
        ([], 0),
        ([-1, -2, -3], -6)
    ]
    
    for case, expected in test_cases:
        result = calculate_sum(case)
        print(f"Input: {case} -> Expected: {expected}, Result: {result} | {'✅' if result == expected else '❌'}")
