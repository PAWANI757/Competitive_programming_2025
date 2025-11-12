N = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))
for start in range(N):
        for end in range(start, N):
            # Print elements from start to end
            print(*arr[start:end+1])