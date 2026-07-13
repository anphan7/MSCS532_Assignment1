import random
import sys
import time
import tracemalloc

from quicksort import QuickSort
from merge_sort import MergeSort


def makeDatasets(size):
    randomData = [random.randint(0, size * 10) for _ in range(size)]
    sortedData = sorted(randomData)
    reverseData = sorted(randomData, reverse=True)
    return {"sorted": sortedData, "reverse": reverseData, "random": randomData}


def measure(sorter, data):
    arr = list(data)
    tracemalloc.start()
    start = time.perf_counter()
    sorter.sort(arr)
    elapsed = time.perf_counter() - start
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return elapsed, peak


def main():
    sys.setrecursionlimit(100000)
    sizes = [1000, 10000]
    algorithms = {"QuickSort": QuickSort(), "MergeSort": MergeSort()}
    print(f"{'Algorithm':<10} {'Dataset':<9} {'Size':>7} {'Time(ms)':>10} {'Peak(KB)':>10}")
    for size in sizes:
        datasets = makeDatasets(size)
        for name, data in datasets.items():
            for algoName, sorter in algorithms.items():
                elapsed, peak = measure(sorter, data)
                print(f"{algoName:<10} {name:<9} {size:>7} {elapsed*1000:>10.2f} {peak/1024:>10.1f}")


if __name__ == "__main__":
    main()
