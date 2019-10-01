a=[4,33,56,78]
b=[13,29,41,984]
c=[]
n = len(a)
m = len(b)
i=0;j=0
while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i+=1
    elif a[i] > b[j]:
        c.append(b[j])
        j+=1
    else:
        c.append(a[i])
        i+=1
        j+=1
while i < n :
    c.append(a[i])
    i+=1
while j < n :
    c.append(b[j])
    j+=1
print(c)
    