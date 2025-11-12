A = "aabbcc"
B = 98
ch = chr(B)
if ch in A:
    print(A.index(ch))
else:
    print(-1)