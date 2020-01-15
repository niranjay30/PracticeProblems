def fib(n):
    first = 0
    second = 1
    print(first, second, end=" ")

    for i in range(n):
        next = first + second
        print(next, end=" ")
        first = second
        second = next


n = int(input("Enter how many numbers of the series you want:"))

fib(n)
