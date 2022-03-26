# Smallest Subarray with a given sum
# ----------------------------------------------------------------
# Given an array of integers and a number k, find the length of smallest
# subarray with sum greater than or equal to the given value.
# ----------------------------------------------------------------
# The idea is having two variables that hold the index of "start" and "end" of the window
# while current sum smaller than k, we keep increase end. When the condition fails, we update sum (if needed)
# and increase start, and then update start (inside condition sum > k). This will make the condition fails again, and we repeat the process.
def solution(array, k):
    n = len(array)
    curr_sum = 0
    min_len = n + 1

    # Initialize starting and ending indekes
    start = 0
    end = 0
    while (end < n):

        # Keep adding array elements while current
        # sum is smaller than or equal to k
        while (curr_sum <= k and end < n):
            curr_sum += array[end]
            end += 1

        # If current sum becomes greater than k.
        while (curr_sum > k and start < n):

            # Update minimum length if needed
            if (end - start < min_len):
                min_len = end - start

            # remove starting elements
            curr_sum -= array[start]
            start += 1

    return min_len


# arr[] = {1, 4, 45, 6, 0, 19}
#    x  =  51
# Output: 3
# Minimum length subarray is {4, 45, 6}

# arr[] = {1, 10, 5, 2, 7}
#    x  = 9
# Output: 1
# Minimum length subarray is {10}

# arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
#     x = 280
# Output: 4
# Minimum length subarray is {100, 1, 0, 200}

# arr[] = {1, 2, 4}
#     x = 8
# Output : Not Possible
# Whole array sum is smaller than 8.

def main():
    arr1 = [1, 4, 45, 6, 10, 19]
    k = 51
    res1 = solution(arr1, k)

    print(res1)


main()
