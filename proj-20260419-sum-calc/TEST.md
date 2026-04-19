# Test Plan for proj-20260419-sum-calc

## Verification Commands
```bash
python3 /home/node/.openclaw/workspace/proj-20260419-sum-calc/sum_calc.py
```

## Test Cases
1. **Integers**: `add(1, 2)` -> Expected: `3`
2. **Floats**: `add(1.5, 2.5)` -> Expected: `4.0`
3. **Mixed**: `add(1, 2.5)` -> Expected: `3.5`
4. **Negative**: `add(-1, -1)` -> Expected: `-2`
5. **Invalid Input**: `add("1", 2)` -> Expected: `TypeError`
