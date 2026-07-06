import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from insertion_sort import InsertionSort

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE, "inputs")
EXPECTED_DIR = os.path.join(BASE, "expected")


def loadNumbers(path):
    with open(path) as f:
        return [int(x) for x in f.read().split(",")]


def main():
    sorter = InsertionSort()
    testFiles = sorted(os.listdir(INPUT_DIR))
    passed = 0

    for name in testFiles:
        numbers = loadNumbers(os.path.join(INPUT_DIR, name))
        expected = loadNumbers(os.path.join(EXPECTED_DIR, name))
        result = sorter.sort(numbers)

        if result == expected:
            passed += 1
            print(f"✅ {name}")
        else:
            print(f"❌ {name}  got {result}  expected {expected}")

    total = len(testFiles)
    print(f"\n{passed}/{total} tests passed")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
