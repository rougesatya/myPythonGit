"""
A function to find the sqaure root of a number
"""

def sqr_root(num1):
    return num1*num1


def test_sqr_root():
    assert sqr_root(7)==49
    assert sqr_root(13)==169
    assert sqr_root(5)==25
    print("THE FUNCTION DEFINATION IS CORRECT")

test_sqr_root()
