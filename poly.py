class poly: 

    def __init__(self,*termpairs):

        self.termpairs = termpairs
        self.exponets = []
        self.coeffs =self.getcoefflistfromtermlist(self.termpairs)

        
    

        


        

        print("coeffs list is ")
        print (self.coeffs)

            
        
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
        return str (self.termpairs)+ str(self.coeffs)
    
    def getstringterm(self,coeff,exponet): 
        if coeff !=  0 and exponet != 0 :
            return str(coeff) + 'x'+ '^' + str(exponet ) 
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




        
         










    

 

    
    
    

    

    

    
    
