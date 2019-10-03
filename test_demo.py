import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    assert demo.add(2,4)==6

def test_sub():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    assert demo.sub(2,4)==-2

