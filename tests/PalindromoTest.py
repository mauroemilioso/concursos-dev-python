import sys
import os
import unittest

from src.Palindromo import Palindromo

class PalindromoTest(unittest.TestCase):

    #def __init__(self):
        #Não tem implementação 
   
    def testNaoEhPalindromo(self):
        palindromo = Palindromo()
        result = palindromo.ehpalindromo("Mauro")
        self.assertEqual(result,False)

    def testEhPalindromo(self):
        palindromo = Palindromo()
        result = palindromo.ehpalindromo("analina")
        self.assertEqual(result,True)

    if __name__ == '__main__':
        unittest.main

        


