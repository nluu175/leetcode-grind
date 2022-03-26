# Maximum Sum Subarray of Size
# ----------------------------------------------------------------
# Given an array of integers and a number k, find the maximum sum of a subarray of size k.
# ----------------------------------------------------------------
def solution(array, k):
    if len(array) < k:
        return 0

    max_sum = 0
    # Get max sum of the first window
    for i in range(k):
        max_sum += array[i]

    for i in range(k, len(array)):
        max_sum = max(max_sum, max_sum - array[i - k] + array[i])

    return max_sum


def main():
    # Test suite
    array = [100, 200, 300, 400]
    k = 2
    assert 700 == solution(array, k)

    array = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert 39 == solution(array, k)

    array = [2, 3]
    k = 3
    assert 0 == solution(array, k)


main()
