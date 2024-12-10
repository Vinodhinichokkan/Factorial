#progarm to printfactorial of a number recursively

#recusive function

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)
    
#user input

num = 7

#check if the input is valid or not

if num<0:
    print("Invalid input ! Please enter a positive number")
elif num == 0:
    print("Factorial of a number 0 is 1")

else:
    print("Factorial of number", num, "=",recursive_factorial(num))  # o/p is Factorial of number 7 = 5040
