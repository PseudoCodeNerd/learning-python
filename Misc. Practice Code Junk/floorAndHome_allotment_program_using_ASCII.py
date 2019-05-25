'''Program No:10
    Developed by: Madhav S.Sharma
    Class Section: XI I
    Date: 10 April 2019'''
    #DOUBT

cnum=int(input("Enter Customer Number: "))
block=chr(65 + (cnum-1)//5)
floor=(cnum-1)%5
print("Your Block: ", (block))
print("Your Floor: ", (floor))
print("You live in Block ",(block) ,"on", (floor),"floor.")

#Enter Customer Number: 10
#Your Block:  B
#Your Floor:  4
#You live in Block  B on 4 floor.