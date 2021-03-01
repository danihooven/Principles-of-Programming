
def is_triangle(a, b, c):
    """"
    Triangle Inequality Theorem
    this function will take 3 length parameters, and determine if three sides can form a triangle
    :param a: float
    :param b: float
    :param c: float
    :return: true or false
    """
    if (a < (b + c)) and (b < (c + a)) and (c < (a + b)): #the sum of two sides is greater than the third
        return True
    else:
        return False