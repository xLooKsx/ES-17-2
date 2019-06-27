import pytest
from principal import somar
from principal import subtrair

def testeSomar():
    assert somar(2, 4)==6

def testeSub():
    assert subtrair(2, 2)==0