def subarray_sum(arr, L, R):
    return sum(arr[L-1:R])

N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))
L, R = map(int, input("Enter L and R: ").split())

print(subarray_sum(arr, L, R))