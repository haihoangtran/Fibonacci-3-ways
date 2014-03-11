from RecursiveFibonacci import *
class MemoizedRecursiveFibonacci(RecursiveFibonacci):
    def __init__(self):
        self.memoizedList = {0:1, 1:1}

    def getValueAt(self, position):
        if position not in self.memoizedList:
            self.memoizedList[position] = super(MemoizedRecursiveFibonacci, self).getValueAt(position)
        return self.memoizedList[position]
    