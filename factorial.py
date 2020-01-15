def fact(n):

    result = 1

    if n >= 0:
        for i in range(1, n+1):

            result = result * i

        print(result)
    else:
        print("Please enter a positive number")


number = int(input("Enter a number : "))
fact(number)