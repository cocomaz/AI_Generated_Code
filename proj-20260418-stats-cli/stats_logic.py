def calculate_stats(numbers):
    """
    Calculate the sum and average of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        tuple: (sum, average) or (0, 0) if the list is empty.
    """
    if not numbers:
        return 0, 0.0
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    return total_sum, average

if __name__ == "__main__":
    # Test cases for verification
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [],
        [5.5, 4.5, 10]
    ]
    
    for case in test_cases:
        s, a = calculate_stats(case)
        print(f"List: {case} -> Sum: {s}, Avg: {a}")
