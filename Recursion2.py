def sum(n):
    if (n==0):
        return 0
    return n + sum(n-1)

a = int(input("Enter number : "))
print(f"Sum of all natural number upto the given number is {sum(a)}")

