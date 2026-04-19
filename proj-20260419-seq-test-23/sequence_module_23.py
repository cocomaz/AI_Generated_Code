def get_numbers_forward():
    """
    Returns a list of integers from 1 to 23.
    """
    return list(range(1, 24))

if __name__ == "__main__":
    # Test the function
    result = get_numbers_forward()
    print(f"Result: {result}")
    assert result == list(range(1, 24)), "Sequence mismatch!"
    print("Verification successful!")
