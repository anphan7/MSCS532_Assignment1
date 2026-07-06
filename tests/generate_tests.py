"""Generate 50 test cases for insertion sort (monotonically decreasing order).

Each test case produces two files:
  inputs/test_XX.txt    -> a list of unsorted integers (comma-separated)
  expected/test_XX.txt  -> the same integers sorted in DECREASING order

A fixed random seed is used so the tests are reproducible.
"""

import os
import random

random.seed(532)  # reproducible: same tests every time this runs

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE, "inputs")
EXPECTED_DIR = os.path.join(BASE, "expected")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(EXPECTED_DIR, exist_ok=True)

NUM_TESTS = 50

for i in range(1, NUM_TESTS + 1):
    size = random.randint(1, 20)
    numbers = [random.randint(-100, 100) for _ in range(size)]
    expected = sorted(numbers, reverse=True)  # monotonically decreasing

    name = f"test_{i:02d}.txt"
    with open(os.path.join(INPUT_DIR, name), "w") as f:
        f.write(",".join(str(n) for n in numbers) + "\n")
    with open(os.path.join(EXPECTED_DIR, name), "w") as f:
        f.write(",".join(str(n) for n in expected) + "\n")

print(f"Generated {NUM_TESTS} test cases in {INPUT_DIR} and {EXPECTED_DIR}")
