lis = [34,1,53,754,2355,85,32,65,2,167,8,3114,6421]

print("Demo of Insertion Sort\n")
n = len(lis)
for i in range(1, n):
    temp = lis[i]
    for j in range(i-1,-1,-1):
        if lis[j] > temp:
            lis[j+1] = lis[j]
        else:
            lis[j+1] = temp
            break
print(lis)
