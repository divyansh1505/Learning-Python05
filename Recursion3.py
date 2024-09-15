def star(n):
    if (n==0):
        return "Thank you"
    print("*"*n)
    star(n-1)

a=int(input("Enter number : "))
print(star(a))

    