def add(a, b):
    """
    Returns the sum of two numbers (int or float).
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be integers or floats")
    return a + b

if __name__ == "__main__":
    # Basic tests
    print(f"1 + 2 = {add(1, 2)}")       # Expected: 3
    print(f"1.5 + 2.5 = {add(1.5, 2.5)}") # Expected: 4.0
    print(f"-1 + 5 = {add(-1, 5)}")     # Expected: 4
