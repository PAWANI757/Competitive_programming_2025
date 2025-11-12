N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

for start in range(N):
        curr_sum = 0
        for end in range(start, N):
            curr_sum += arr[end]
            print(curr_sum)