import sys


class QuickSort:
    def sort(self, arr):
        self._quicksort(arr, 0, len(arr) - 1)
        return arr

    def _quicksort(self, arr, low, high):
        while low < high:
            pivotIndex = self._partition(arr, low, high)
            if pivotIndex - low < high - pivotIndex:
                self._quicksort(arr, low, pivotIndex - 1)
                low = pivotIndex + 1
            else:
                self._quicksort(arr, pivotIndex + 1, high)
                high = pivotIndex - 1

    def _partition(self, arr, low, high):
        mid = (low + high) // 2
        pivot = arr[mid]
        arr[mid], arr[high] = arr[high], arr[mid]
        storeIndex = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
                storeIndex += 1
        arr[storeIndex], arr[high] = arr[high], arr[storeIndex]
        return storeIndex


def main():
    text = sys.stdin.read()
    numbers = [int(x) for x in text.split(",")]
    sortedNumbers = QuickSort().sort(numbers)
    result = ",".join(str(n) for n in sortedNumbers)
    print(result)


if __name__ == "__main__":
    main()
