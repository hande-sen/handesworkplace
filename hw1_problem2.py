# Write a program that generates a list of 20 random numbers between 1 and 100. When generating
# random number use random seed as 18.
# (a) Print the list.
# (b) Print the sorted list (sort list in the descending order)
# (c) Print the average of the elements in the list.
# (d) Print how many even numbers are in the list.
# (e) Print the largest and smallest values in the list.
# (f) Print the second largest and second smallest entries in the list

import  random
def findEven(lst):
    total = 0
    for i in lst:
        if i%2==0:
            total+=1
    return total

def  secondLarge(lst):
    l1 = max(lst)
    newLst=sorted(lst,reverse=True)
    for i in newLst:
        if i<l1:
            break
    return(i)

def  secondSmall(lst):
    s1 = min(lst)
    newLst=sorted(lst)
    for i in newLst:
        if i>s1:
            break
    return(i)
            

lst = []
for x in range(20):
  lst.append(random.randint(1,100))
print("The numbers in the list:" ,lst)
print("The sorted list:", sorted(lst))
print("The average of the list: ", sum(lst)/len(lst))
print("The number of even-numbers is: ", findEven(lst))
print("The largest element of the list: ", max(lst))
print("The smallest element of the list: ", min(lst))
print("The second largest element of the list:" ,secondLarge(lst))
print("The second smallest element of the list:" ,secondSmall(lst))


