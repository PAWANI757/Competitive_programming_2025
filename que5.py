def max_subarray_sum(arr, N):
    max_ending_here = arr[0]
    max_so_far = arr[0]
    
    for i in range(1, N):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

print(max_subarray_sum(arr, N))