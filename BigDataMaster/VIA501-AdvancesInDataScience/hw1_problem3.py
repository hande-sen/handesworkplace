def createFibonacci(n):
    lst = [1,1]
    for _ in range(n-2):
        lst.append(lst[-1]+lst[-2])
    return(lst)

n=int(input("How many Fibonacci numbers do you want:"))
print(createFibonacci(n))
