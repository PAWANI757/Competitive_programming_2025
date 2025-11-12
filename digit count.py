# Kisi number ke digits count karna
n = int(input("Enter a number: "))
a = 0
while n > 0:
    a = a + 1
    n = n // 10
print(a)
