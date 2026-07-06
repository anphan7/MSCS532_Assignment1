import sys


class InsertionSort:
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


def main():
    text = sys.stdin.read()
    numbers = [int(x) for x in text.split(",")]
    sortedNumbers = InsertionSort().sort(numbers)
    result = ",".join(str(n) for n in sortedNumbers)
    print(result)


if __name__ == "__main__":
    main()
