A = [1, 2, 3, 4, 5]
print(*[x for x in A if x % 2 != 0])  # 1 3 5
print(*[x for x in A if x % 2 == 0])  # 2 4
