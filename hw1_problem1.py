# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the
# cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that takes
# how many items are bought and prints the total cost.
def total_cost(n):
    cost = 0
    if n<10:
        cost = n*12
    elif n>=10 and n<=99:
        cost = n*10
    else:
        cost = n*7
    return cost

n=int(input("How many items do you want to buy: "))
print("Total cost is $",total_cost(n))