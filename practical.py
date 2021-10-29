num=int(input(print("Enter a number\n")))

factorial = 1

if num < 0:
    print("Number is negative,hence no factorial.")

elif num ==0:
    print("The factorial is 1")

else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial is ",factorial)