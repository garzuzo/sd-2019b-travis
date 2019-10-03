import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    add_result = demo.add(3,4)
    assert demo.add(2,4)==6

