A = [1, 2, 3, 4]
even = len([x for x in A if x % 2 == 0])
odd = len([x for x in A if x % 2 != 0])
print(abs(even - odd))  # Output: 0
