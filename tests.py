""" Tests for maths.py """
import pytest

def test_ordenarArray():
    """ Test sumando 2 numeros """
    numeros = [1, 3, 5, 7, 9]
    assert 9 == ordenarArray(numeros)

def ordenarArray(array):
    mayor = 0
    for x in array:
        if x > mayor:
            mayor = x
    return x
