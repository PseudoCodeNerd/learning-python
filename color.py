import sys
print('')
print("Favorite Color Guessing Machine")
print('')
print("This program will only be able to guess if your color is in the rainbow, or is gray,black,pink,brown or white.")
print('')
color_type = input("Is your color a warm color, a cold color, a neutral color, or none of the above?")
if color_type == "cold":
    print('')
    cold1 = input("is your color a sky color, a ground color, or neither? answer with ground, sky, or neither.")
    if cold1 == 'ground':
        print('')
        print("your color is green.")
        sys.exit("Your color is green.")
    if cold1 == "sky":
        print('')
        print("your color is blue")
        print('')
        sys.exit("Your color is blue.")
    if cold1 == "neither":
        print('')
        violet_indigo = input("is your color commonly associated with grapes?")
        if violet_indigo == "yes":
            print('')
            print("your color is violet.")
            sys.exit("your color is violet.")
        if violet_indigo == "no":
            print('')
            print("your color is indigo.")
            sys.exit("your color is indigo.")
if color_type == "neutral":
    print('')
    neut1 = input("is your color a mix of two neutral colors?")
    if neut1 == "yes":
        print('')
        print("Your color is gray.")
        sys.exit("your color is gray.")
    elif neut1 == "no":
        print('')
    neut2 = input("is your color a dark color, or a light color? answer by saying dark or light.")
    if neut2 == "dark":
        print('')
        print("your color is black.")
        sys.exit("your color is black.")
    elif neut2 == "light":
        print('')
        print("your color is white.")
        sys.exit("your color is white.")
if color_type == "warm":
    print('')
    warm1 = input("is your color the first color of the rainbow?")
    if warm1 == "yes":
        print('')
        print("your color is red.")
        sys.exit("your color is red.")
    elif warm1 == "no":
        print('')
        warm2 = input("is your color also a name of a fruit?")
        if warm2 == "yes":
            print('')
            print("your color is orange.")
            sys.exit("your color is orange.")
        elif warm2 == "no":
            print('')
            print("your color is yellow.")
            sys.exit("your color is yellow.")
            if color_type == "none of the above":
    print('')
    nota = input("is your color a mix of 2 colors?")
    if nota == "yes":
        print('')
        notaquest = input("is your color often associated with breast cancer?")
        if notaquest == "yes":
            print('')
            print("your color is pink.")
            sys.exit("your color is pink.")
    if nota == "no":
        print('')
        nota2 = input("does your color remind you of a chocolate? ")
        if nota2 == "yes":
            print('')
            print("your color is brown.")
            sys.exit("your color is brown.")
        elif nota2 == "no":
            print("sorry, but we couldn't find your favorite color.")