# 1 se A tak ke even numbers ka sum

a = int(input("Enter a number: "))
s = 0
for i in range(2, a+1, 2):
    s += i
print("Sum of even numbers =", s)
