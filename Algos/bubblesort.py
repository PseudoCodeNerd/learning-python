lis = []
cont = True
while cont:
  elem = int(input("Enter number to list: "))
  lis.append(elem)
  yorn = str(input("Add another element ? "))
  if yorn[0] == 'y' or yorn[0] == 'Y':
    pass
  else:
    cont = False
print("Demo of Bublle Sort")
lens = len(lis)
for i in range(0, lens):
  for j in range(0, lens-1-i):
    if lis[j] > lis[j+1]:
      lis[j], lis[j+1] = lis[j+1], lis[j]
print("Sorted List: ", lis)