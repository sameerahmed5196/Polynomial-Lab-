

from poly import *

if __name__ == "__main__":
    P = poly((-7,8),(9,4),(-9,15))

    
    print(P.getstringterm(4,0))
    print(P.getstringterm(4,3))
    print(P.getstringterm(-4,3))
    print(P.getstringterm(0,3))
    result = P.multiplyterms(4,2,3,5)
    print(P.getstringterm(result[0],result[1]))
    print('Print of poly')
    print (P)
    print(P.degree())



P = poly((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print (P)
print(P.evaluate(2))




P = poly((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print(P)
P.addterm(5,5)
print(P)
P.addterm(5, 20)
print(P)


P = poly((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print('after deleten lowest term')
P.addterm(9,0)
print(P)

P = poly((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print ('after deleting highest term')
P.removeterm(6)
print (P)

P = poly((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print ('before ')
print (P)
print ('after deleting middle term')
P.removeterm(4)
print (P)

