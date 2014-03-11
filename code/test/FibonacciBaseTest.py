import unittest
from IterativeFibonacci import * 

class FibonacciBaseTest(unittest.TestCase, object):    
    def setUp(self):
        self.fibonacci = self.getClassInstance()
    
    def getClassInstance(self):
        return IterativeFibonacci()
        
    def canary_test(self):
        self.assertTrue(True)
        
    def test_Fibonacci_get_num_at_position_0(self):
        self.assertEquals(1, self.fibonacci.getValueAt(0))
          
    def test_Fibonacci_get_num_at_position_1(self):
        self.assertEquals(1, self.fibonacci.getValueAt(1))
        
    def test_Fibonacci_get_num_at_position_2(self):
        self.assertEquals(2, self.fibonacci.getValueAt(2))
        
    def test_Fibonacci_get_num_at_position_3(self):
        self.assertEquals(3, self.fibonacci.getValueAt(3))
        
    def test_Fibonacci_get_num_at_position_4(self):
        self.assertEquals(5, self.fibonacci.getValueAt(4))
        
    def test_Fibonacci_get_num_at_position_5(self):
        self.assertEquals(8, self.fibonacci.getValueAt(5))
        
    def test_Fibonacci_get_num_at_position_6(self):
        self.assertEquals(13, self.fibonacci.getValueAt(6))
    
    def test_Fibonacci_get_num_at_negative_position(self):
        self.assertEquals(1, self.fibonacci.getValueAt(-1))
        
