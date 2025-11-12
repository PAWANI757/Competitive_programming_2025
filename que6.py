def total_subarray_sum(arr, N):
    total = 0
    for i in range(N):
        total += arr[i] * (i + 1) * (N - i)
    return total


N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

print(total_subarray_sum(arr, N))
