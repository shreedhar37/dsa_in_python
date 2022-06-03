def fact(n):

    if n == 0 or n == 1:
        return 1 
    
    elif n > 1:
        return n * fact(n-1)


if __name__ == "__main__":
    
    n = int(input("Enter the number : "))

    if fact(n) == True:

        print("The factorial of the {} is {}".format(n, fact(n)))
    
    else:
        print("Can't find the factorial of the negative number!!!")