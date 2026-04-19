# Project: Number Printer 36
# Project ID: proj-20260419-num-print-36

## Task: task-20260419-num-36-02 - Implement Unit Test for print_numbers
- **Goal**: Verify that `print_numbers()` correctly outputs numbers from 1 to 36.
- **Implementation Plan**:
    1. Create `test_num_print.py` using the `unittest` framework.
    2. Use `unittest.mock.patch` and `io.StringIO` to capture `sys.stdout`.
    3. Compare the captured output with the expected range of numbers [1, ..., 36].
- **Dependencies**: `unittest` (Standard Library)
- **Estimated Time**: 10 minutes
