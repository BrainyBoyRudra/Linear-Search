def linearsearch (n,array):
    for i in range(len(array)):
        if array[i]==n:
            return i
    return -1
array=[67,83,54,15,91,48,28,100,88,21,17,31,25]
print('Hi Im The Searching Bot')
n = int(input('Please enter the number value to search. '))
output = linearsearch(n,array)
if output == (-1):
    print('The Value you searched was Not found (Error 402)')
else :
    print('Your Search was succesful The index value of your search is' ,output+1)