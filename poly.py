class poly: 

    def __init__(self,*termpairs):

        self.termpairs = termpairs
        self.exponets = []
        self.coeffs = []

        for x in self.termpairs :

            self.coeffs.append(x[0]) 

        for x in self.termpairs :

            self.exponets.append(x[1])

        size  = (max(self.exponets) + 1) - len(self.coeffs)

        for x in range(size):
            self.coeffs.append(0)
        print (self.coeffs)

        #for x in self.exponets:
            
        

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



        
         










    

 

    
    
    

    

    

    
    
