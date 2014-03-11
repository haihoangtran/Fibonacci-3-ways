class IterativeFibonacci(): 
    def getValueAt(self, position):  
        term1 = 1
        term2 = 1    
        for i in range (2, position + 1):
            result = term1 + term2
            term2 = term1
            term1 = result
        return term1