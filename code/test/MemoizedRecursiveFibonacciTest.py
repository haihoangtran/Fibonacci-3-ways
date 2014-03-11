import unittest
import time
from MemoizedRecursiveFibonacci import * 
from RecursiveFibonacci import *
from FibonacciBaseTest import *

class MemoizedRecursiveFibonacciTest(FibonacciBaseTest): 
    def getClassInstance(self):
        return MemoizedRecursiveFibonacci()
    
    def test_performance_comparison_between_recursive_and_memoized_versions_with_position_20(self):
        start = time.clock()
        self.fibonacci.getValueAt(20)
        memoizedFibonacciElapsedTime = time.clock() - start
        
        start = time.clock()
        RecursiveFibonacci().getValueAt(20)
        recursiveFibonacciElapsedTime = time.clock() - start
  
        self.assertTrue((recursiveFibonacciElapsedTime/memoizedFibonacciElapsedTime) > 10)
