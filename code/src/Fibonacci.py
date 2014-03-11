class iterativeFibonacci(): 
    def getValueAt(self, position):
        term1 = 1
        term2 = 1
        for i in range (2, position + 1):
            result = term1 + term2
            term2 = term1
            term1 = result
        return term1
        
class recursiveFibonacci():
    def getValueAt(self, position):
        if position < 2:
            return 1 
        return self.getValueAt(position-1) + self.getValueAt(position-2)
        
class memorizedFibonacci():
    def __init__(self):
        self.memorizedList = {}
        
    def getValueAt(self, position):
        if position not in self.memorizedList:
            if position < 2:
                self.memorizedList[position] = 1
            else:
                self.memorizedList[position] = self.getValueAt(position - 1) + self.getValueAt(position - 2)
        return self.memorizedList[position]  

                
