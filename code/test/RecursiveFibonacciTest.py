import unittest
from RecursiveFibonacci import * 
from FibonacciBaseTest import *

class RecursiveFibonacciTest(FibonacciBaseTest):  
    def getClassInstance(self):
        return RecursiveFibonacci()
        