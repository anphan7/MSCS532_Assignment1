# MSCS532 — Algorithms Coursework

Python implementations of sorting algorithms and their analysis for MSCS532.

## Assignment 1 — Insertion Sort

Insertion sort that sorts an array into **monotonically decreasing** order.

- `assignment_1/insertion_sort.py` — the `InsertionSort` class and a `main` that
  reads comma-separated numbers from stdin and prints them sorted in decreasing order.
- `assignment_1/tests/generate_tests.py` — generates 50 test cases (reproducible, fixed seed).
- `assignment_1/tests/inputs/` — 50 input files of unsorted numbers.
- `assignment_1/tests/expected/` — matching expected outputs, sorted in decreasing order.
- `assignment_1/tests/run_tests.py` — runs all 50 tests and reports pass/fail.

```
echo "5,2,9,1,7,3" | python3 assignment_1/insertion_sort.py
cd assignment_1 && python3 tests/run_tests.py
```

## Assignment 2 — Quicksort vs. Merge Sort

Quicksort and merge sort implementations with a performance comparison.

- `assignment_2/quicksort.py` — the `QuickSort` class (in-place).
- `assignment_2/merge_sort.py` — the `MergeSort` class.
- `assignment_2/benchmark.py` — benchmarks both on sorted, reverse-sorted, and
  random datasets, measuring execution time and peak memory.
- `assignment_2/analysis.txt` — results and discussion of theory vs. practice.

```
echo "5,2,9,1,7,3" | python3 assignment_2/quicksort.py
echo "5,2,9,1,7,3" | python3 assignment_2/merge_sort.py
python3 assignment_2/benchmark.py
```

## Requirements

Python 3. No third-party dependencies.
