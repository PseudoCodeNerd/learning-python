'''
Create a list and:
1. display smallest value in given list
2. highest value in a given list
3. second highest value in a given list
'''

my_lis= [10,34,46,54,2,59,86,19,32,76,97]

minmum = my_lis[0]
lenList = len(my_lis)
for i in range(lenList):
    if my_lis[i] < minmum:
        minmum = my_lis[i]
print("Smallest Value in List is : ", minmum)

maxnum = my_lis[0]
for j in range(lenList):
    if my_lis[j] > maxnum:
        maxnum = my_lis[j]
print("Largest value in the given list is : ", maxnum)


def findMaxList(mah_lis):
    mah_lis = mah_lis
    maxnumF = 0
    lenMahList = len(mah_lis)
    for k in range(lenList):
        if mah_lis[k] > maxnumF:
            maxnumF = mah_lis[k]
    return maxnumF



new_lis = my_lis
maxnum3 = my_lis[0]
for j in range(lenList):
    if my_lis[j] > maxnum3:
        maxnum3 = my_lis[j]
new_lis.remove(maxnum3)
lenList2 = len(new_lis)
secmax = new_lis[0]
for j in range(lenList2):
    if new_lis[j] > secmax:
        secmax = new_lis[j]
print("Second Highest Number : ", secmax)


