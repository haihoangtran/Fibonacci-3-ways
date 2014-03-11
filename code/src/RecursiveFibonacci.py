class RecursiveFibonacci(object):
    def getValueAt(self, position):
        if position < 2:
            return 1 
        return self.getValueAt(position-1) + self.getValueAt(position-2)