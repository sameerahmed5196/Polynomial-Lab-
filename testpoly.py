"""
Object Oriented Programming, Fall 2020
Test module for Problem 3, Assignment #4
"""

from poly import *


if __name__ == "__main__":
    answer = "y"
    while (answer[0].lower() == "y"):
        print("                  ----------------------------")
        print("                   Testing Polynomial methods ")
        print("                  ----------------------------")
        print(" ")
        print("I will create two polynomials. The first polynomial")
        print("is created using the constructor, and the second")
        print("polynomial is read from a file. You will be asked")
        print("to provide the name of the file containing the")
        print("polynomial data.")
        print(" ")
        P1 = Polynomial((6, 14), (9, 11), (-12, 3), (42, 0))
        print("The first polynomial has been created using the constructor.")
        print("It is printed below: ")
        print(P1)
        print(" ")
        filename = input("Enter the name of a file: ")
        P2 = read_polynomial(filename)
        print("The second polynomial has been read from a file.")
        print("It is printed below: ")
        print(P2)
        print(" ")
        print("Each of the Polynomial method implementations will")
        print("now be tested. Check the output to make sure that ")
        print("your function is producing the correct answer.")

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                     Testing degree, evaluate")
        print("                  ------------------------------")
        print("The degree of the first polynomial is ", P1.degree())
        print("The first polynomial evaluated at x = 0 gives ", P1.evaluate(0))
        print("The first polynomial evaluated at x = 2 gives ", P1.evaluate(2))
        print("The first polynomial evaluated at x = -1 gives ", P1.evaluate(-1.0))

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------------")
        print("                   Testing addterm, removeterm  ")
        print("                  ------------------------------")
        print("I am adding the term 6x^5 to the first polynomial.")
        P1.addterm(6, 5)
        print("The first polynomial is now: ")
        print(P1)
        print("I am removing the term with exponent 5 from the first polynomial.")
        P1.removeterm(5)
        print("The first polynomial is now: ")
        print(P1)

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  -------------------")
        print("                     Testing scale   ")
        print("                  -------------------")    
        sP = P1.scale(2)
        print("The first polynomial scaled by 2 is as follows:")
        print(sP)

        print(" ")
        dummy = input("Hit the enter key to continue.")
        print(" ")
        print("                  ----------------------------------------------")
        print("                    Testing the arithmetic operators (+, -, *)  ")
        print("                  ----------------------------------------------")    
        arith_ops_polys(P1, P2)

        print(" ")
        dummy = input("Hit the enter key to continue.")
        print(" ")
        print("                  -----------------------------------------")
        print("                     Testing __getitem__ and __setitem__   ")
        print("                  -----------------------------------------")    
        print(" ")
        print("I will use the index operator [] (__getitem__) to print")
        print("all the non-zero coefficients of the polynomial P1 below: ")
        for i in range(P1.degree() + 1):
            if P1[i] != 0:
                print(P1[i], end = " ")
        print(" ")
        print("I will now use item assignment (__setitem__) to change")
        print("all coefficients of the polynomial P1 to 1: ")
        for i in range(P1.degree() + 1):
            if P1[i] != 0:
                P1[i] = 1
        print("Polynomial P1 is printed below:")
        print(P1)
        answer = input("Run the tests again? [y/n] ")
        answer += ' '
            
    
    print("Goodbye!!")
    
