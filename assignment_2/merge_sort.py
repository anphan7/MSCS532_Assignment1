import sys


class MergeSort:
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        leftHalf = self.sort(arr[:mid])
        rightHalf = self.sort(arr[mid:])
        return self._merge(leftHalf, rightHalf)

    def _merge(self, left, right):
        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


def main():
    text = sys.stdin.read()
    numbers = [int(x) for x in text.split(",")]
    sortedNumbers = MergeSort().sort(numbers)
    result = ",".join(str(n) for n in sortedNumbers)
    print(result)


if __name__ == "__main__":
    main()
