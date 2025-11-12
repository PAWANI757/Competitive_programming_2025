A = "aeiOUz"
A = A + A
A = "".join(ch for ch in A if not ch.isupper())
A = "".join("#" if ch in "aeiou" else ch for ch in A)
print(A)