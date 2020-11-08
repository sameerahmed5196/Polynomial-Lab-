class Polynomial: 

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

        for x in self.exponets:
            
        

        

        

        
            
            
            

        
        
            


        




    def __str__(self):
        return str (self.termpairs)+ str(self.coeffs)
        
         


P = Polynomial((2,8),(9,4),(4,15))








    

 

    
    
    

    

    

    
    
