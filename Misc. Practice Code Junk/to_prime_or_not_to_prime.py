def to_prime_or_not_to_prime(number):
    #naive python function to check whether a given number is prime or not...

    #"seldomly asked in interviews"-as stated by Jose.
    for num in range(2, number):
        if number % num == 0:
            print(number, "is not prime.")
            break
    else:
        print(number, "is prime.")


to_prime_or_not_to_prime(69)
to_prime_or_not_to_prime(73)
to_prime_or_not_to_prime(37)
to_prime_or_not_to_prime(12)
print("but am I a dork ?")

import math

def better_to_prime_or_not_to_prime(randomumber):
  if randomumber%2 == 0 and randomumber>2:
    return False
  for numb in range(3, int(math.sqrt(randomumber))+1, 2): 
      if randomumber%2 == 0:
        return False
  return True

better_to_prime_or_not_to_prime(73)
better_to_prime_or_not_to_prime(30)
'''
  This Function is an improvement from the previous function.
  It uses a different approach towards finding a prime number.
  Further step-by-step explaination of each code line in commments.
 starting from 3 beacuse 2 is a prime number by being an even number as well.Then we set the range from 3 to the square root of the number to be tested to lessen down the factors and add one to it and go ahead in jumps of 2 to get only odd numbers'''