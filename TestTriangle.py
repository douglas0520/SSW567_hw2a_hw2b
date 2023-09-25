# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(3,3,4), 'isosceles', '3,3,4 is an isosceles triangle')

    def testScalene(self):
        self.assertEqual(classifyTriangle(5,7,9), 'scalene', '5,7,9 is an scalene triangle')

    def testInputLimitMax(self):
        self.assertEqual(classifyTriangle(300,78,360), 'InvalidInput_Reached_Limit', 'Input_Limit_Reached (> 200)')
    
    def testInputLimitMin(self):
        self.assertEqual(classifyTriangle(-10,10,10), 'InvalidInput_Reached_Limit', 'Input_Limit_Reached (< 0)')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

