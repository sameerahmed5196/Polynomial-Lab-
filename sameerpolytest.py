

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







