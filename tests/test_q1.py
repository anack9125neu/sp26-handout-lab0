"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

def test_palindrome_tacocat()-> None:
    assert is_palindrome("tacocat") == True

def test_palindrome_racecar()-> None:
    assert is_palindrome("racecar") == True

def test_not_palindrome_hello()-> None:
    assert is_palindrome("hello") == False