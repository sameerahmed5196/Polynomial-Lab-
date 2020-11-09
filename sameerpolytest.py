

from poly import *

if __name__ == "__main__":
    P = Polynomial((-7,8),(9,4),(-9,15))

    
    print(P.getstringterm(4,0))
    print(P.getstringterm(4,3))
    print(P.getstringterm(-4,3))
    print(P.getstringterm(0,3))
    result = P.multiplyterms(4,2,3,5)
    print(P.getstringterm(result[0],result[1]))
    print('Print of poly')
    print (P)
    print(P.degree())



P = Polynomial((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print (P)
print(P.evaluate(2))




P = Polynomial((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print(P)
P.addterm(5,5)
print(P)
P.addterm(5, 20)
print(P)


P = Polynomial((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print('after deleten lowest term')
P.addterm(9,0)
print(P)

P = Polynomial((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print ('after deleting highest term')
P.removeterm(6)
print (P)

P = Polynomial((-12,6), (5, 5), (-20, 4), (8, 2), (-12, 1), (9, 0))
print ('before ')
print (P)
print ('after deleting middle term')
P.removeterm(4)
print (P)



output = P.scale(2)
print(output)

P1 = Polynomial((4,0),(10,2),(-4,3),(6,5))
P2  = Polynomial((8,1),(-3,2),(-5,7),(3,9))

print(P1) 
print(P2)
P3 = P1 + P2 
print(P3)
print(P1-P2) 

P1 = Polynomial((1,4),(4,3),(4,2))
P2 = Polynomial((2,1),(-1,0))
print("results")
print(P1)
print(P2)
print (P1 * P2 )

polyFromFile = read_polynomial('poly1.txt')
print(polyFromFile)
polyFromFile = read_polynomial('poly2.txt')
print(polyFromFile)

x = arith_ops_polys(Polynomial((4,0),(10,2),(-4,3),(6,5)),Polynomial((8,1),(-3,2),(-5,7),(3,9)))
print(x)
P = Polynomial((6,5),(1,1),(3,4),(9,8))
P[]
print(R)