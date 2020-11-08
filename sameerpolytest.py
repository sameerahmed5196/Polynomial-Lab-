

from poly import *

if __name__ == "__main__":
    print("hello")
    P = poly((2,8),(9,4),(4,15))

    
    print(P.getstringterm(4,0))
    print(P.getstringterm(4,3))
    print(P.getstringterm(-4,3))
    print(P.getstringterm(0,3))
    result = P.multiplyterms(4,2,3,5)
    print(P.getstringterm(result[0],result[1]))







