''' Sameer Ahmed
    RUID = 202001556
    problem 3 hw 4 


    This class performs multiple tasks in regards to polynomials
    1. create a polynomial object 
    2. perform arithmetic on  polynomial objects 
    3.read and create polynomial objects from a file
    4. scale  a polynomial 
    5. add or remove a term from a polynomial 
'''





class Polynomial: 

    def __init__(self,*termpairs):

        self.termpairs = termpairs
        self.exponets = []
        self.coeffs =self.getcoefflistfromtermlist(self.termpairs)

            
        
    def getmaxexponent(self,*termpairs): 
        exponets = [] 
        for x in self.termpairs :
            exponets.append(x[1])

        return max (exponets)
    
    def getcoefflistfromtermlist(self,*termpairs): 
        size = self.getmaxexponent(termpairs) + 1
        coeffs = [] 

        for x in range(size):
            coeffs.append(self.findcoeffdegree(x))

        return coeffs
        

        


    def __str__(self):
        size = len(self.coeffs)

        index = size - 1 
        expression = ''

        while index>=0:
            if(self.coeffs[index]<0):
                expression =  expression + ' - '
            elif (self.coeffs[index]>0 and index != size - 1):
                expression = expression + ' + '

            expression = expression + self.getstringterm(self.coeffs[index], index)
            index-=1
      
        return expression
    def __repr__(self): 
        str(self)
    
    def getstringterm(self,coeff,exponet): 
        if coeff >  0 and exponet != 0 :
            return  str(coeff) + 'x'+ '^' + str(exponet ) 
        if coeff < 0 and exponet != 0:
            return  str(-1*coeff) + 'x'+ '^' + str(exponet ) 
        elif coeff!= 0 and exponet == 0: 
            return str(coeff)
        
        else: 
            return str("")
    
    def multiplyterms(self,coeff1, degree1,coeff2,degree2): 
        return (coeff1 * coeff2, degree1+degree2)

    def addcoeffs (self,coeff1,coeff2): 
        return (coeff1 + coeff2)

    def canaddterms(self,degree1,degree2): 
        if degree1 == degree2: 
            return True 
        else: 
            return False 

    def scaleold (self,coeff,scale): 
        coeff = coeff * scale 
    
    def subcoeffs (self,coeff1,coeff2): 
        return (coeff1 - coeff2)
    
    def findcoeffdegree(self,degree): 
        for term in self.termpairs: 
            if term[1]  ==  degree : 
                return term[0] 
        return 0 

    def degree(self):
        return len(self.coeffs )- 1
    
    def evaluateterm(self,x,coeff,exponent):
        return coeff * pow(x,exponent)

    def evaluate(self,x): 
        
        result = 0 
        exponent = 0

        for coeff in self.coeffs: 
            
            result += self.evaluateterm(x, coeff, exponent)
            exponent +=1
        
        return result 

        
    def addterm (self,cf,exp): 
        if exp < len(self.coeffs):
            self.coeffs[exp] = self.coeffs[exp] + cf
        else: 
            
            index = len(self.coeffs)

            
            while index < exp + 1 : 
                self.coeffs.append(0)
                index +=1

            self.coeffs[exp] = cf
    
    def removeterm(self,exp):
        if exp >= len(self.coeffs) or exp < 0 : 
            return 
        elif exp == len(self.coeffs)-1:
            del self.coeffs[exp]
        else:
            self.coeffs[exp] = 0 
        
            
    def scale (self,s):
        degree = 0 
        newterms = []
        for x in self.coeffs: 
            x = x * s 
            newterms.append((x, degree))
            degree += 1
        
        
        
        newpolynomial = Polynomial((*newterms))
        return newpolynomial

# other is a polynomial object
    def __add__(self,other): 
        newpoly = self.scale(1)
        degree = 0 
        for coefficent in other.coeffs: 
            newpoly.addterm(coefficent, degree)
            degree += 1 

        return newpoly   
# other is a polynomial object

    def __sub__(self,other): 
        newpoly = self.scale(1)
        degree = 0 
        for coefficent in other.coeffs: 
            newpoly.addterm (-1 *coefficent , degree)
            degree += 1 

        return newpoly  
# other is a polynomial object

    def __mul__(self,other): 
        result = Polynomial((0,0))
        exp = 0 
        selfexp = 0
        otherexp  = 0
        for x in other.coeffs:
            selfexp = 0
            for y in self.coeffs: 
                result.addterm(x * y, selfexp + otherexp) 
                selfexp +=1
            otherexp +=1
        

        return result 


def read_polynomial(fileName):
    f = open(fileName, "r")
    
    line = f.readline()

    termsArray = []

    while(line!=''):
     parseLine = line.split()
    
     if(len(parseLine)>1):
         termsArray.append((int(parseLine[0]), int(parseLine[1])))

     line = f.readline()
    
     
    result = Polynomial((*termsArray))
    


    return result

def arith_ops_polys(P,Q):
    print("The degree of P is {}".format(P.degree()))
    print("The degree of Q is {}".format(Q.degree()))
    print("The sum of P and Q is {}".format(P+Q))
    print("The diffrence of P and Q is {}".format(P-Q))
    print ("The product of P and Q is {}".format(P*Q))

def __getitem__(self,idx): 
     size = len(self.coeffs)
     if idx >= 0 and idx <= (size) - 1:
         return self.coeffs[idx]
     else:
         return 0  


     

def __setitem__(self,idx,value):
    if idx >= 0 and idx <= (size) - 1:
        self.coeffs[idx] = value
    else: 
        self.coeffs.addterm(value,idx )








    
 

        
         










    

 

    
    
    

    

    

    
    
