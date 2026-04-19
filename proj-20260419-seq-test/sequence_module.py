def get_numbers_forward():
    """
    Returns a list of integers from 1 to 20.
    """
    return list(range(1, 21))

def get_numbers_backward():
    """
    Returns a list of integers from 20 down to 1.
    """
    return list(range(20, 0, -1))

if __name__ == "__main__":
    # Test forward sequence
    forward = get_numbers_forward()
    print(f"Forward: {forward}")
    assert forward == list(range(1, 21)), "Forward sequence mismatch!"
    
    # Test backward sequence
    backward = get_numbers_backward()
    print(f"Backward: {backward}")
    assert backward == list(range(20, 0, -1)), "Backward sequence mismatch!"
    
    print("Verification successful!")
