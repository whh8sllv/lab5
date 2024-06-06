import pytest
from myFunc import *


def test_isPrime1():
    assert isPrime(5) == 'prime'

def test_isPrime2():
    assert isPrime(-16) == 'only a natural number can be prime'


def test_factorial1():
    assert factorial(5) == 120

def test_factorial2():
    assert factorial('bugaga') == 'Type Error'