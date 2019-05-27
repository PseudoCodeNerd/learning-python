'''Just for fun!
A function that takes in a single letter, and returns a 5x5 representation of that letter.

DISCLAIMER: A pen and paper was needed to program this.
                Made only till E... further letters to be added proportional to COFFEE.
'''
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
        
print_big('a')  
print("--------")      
print_big('b')
print("---------")   
print_big('c')   
print("---------")   
print_big('d')   
print("---------")   
print_big('e')   

'''
OUTPUT:
  *
 * *
*****
*   *
*   *
--------
****
*   *
****
*   *
****
---------
*****
*
*
*
*****
---------
****
*   *
*   *
*   *
****
---------
*****
*
*****
*
*****
---------

voila!
'''