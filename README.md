# MSCS532_Assignment1

Insertion Sort in Python that sorts an array into **monotonically decreasing** order (MSCS532 Assignment 1).

## Files

- `insertion_sort.py` — the `InsertionSort` class and a `main` that reads comma-separated numbers from stdin and prints them sorted in decreasing order.
- `tests/generate_tests.py` — generates 50 test cases (reproducible, fixed seed).
- `tests/inputs/` — 50 input files of unsorted numbers.
- `tests/expected/` — matching expected outputs, sorted in decreasing order.
- `tests/run_tests.py` — runs all 50 tests and reports pass/fail.

## Usage

Sort a list of numbers:

```
echo "5,2,9,1,7,3" | python3 insertion_sort.py
```

Run the tests:

```
python3 tests/run_tests.py
```
