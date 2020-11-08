class poly: 

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

    def scale (self,coeff,scale): 
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
        elif exp == len(self.coeffs)-1
            self.coeffs.remove(exp)
        else:
            self.coeffs[exp] =0 
        
            

        






        
         










    

 

    
    
    

    

    

    
    
