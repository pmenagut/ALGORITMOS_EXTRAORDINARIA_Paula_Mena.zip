from functools import partial

class MathOperations:
    def multiply(self, x, y):
        """
        Multiply two numbers.

        Parameters
        ----------
        x : int or float
            The first number.
        y : int or float
            The second number.
        """
        return x * y

    def power(self, base, exponent):
        """
        Raise base to the power of exponent.

        Parameters
        ----------
        base : int or float
            The base number.
        exponent : int or float
            The exponent.
            """
        return base ** exponent

    # Specialized functions using functools.partial
    double = partial(multiply, 2)
    square = partial(power, 2)

def main():
    """Function main of the module.

    The function main of this module is used to test the class MathOperations
    and its specialized versions using functools.partial.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """
    math_ops = MathOperations()

    
    print("=================================================================.")
    print("Test Case 1: Double a number.")
    print("=================================================================.")
    try:
        result = math_ops.double(5)
        if result == 10:
            print("Test PASS. The result of doubling 5 is correct.")
            print("Result:", result)
        else:
            print("Test FAIL. The result of doubling 5 is incorrect.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    print("=================================================================.")

    print("Test Case 2: Square a number.")
    print("=================================================================.")
    try:
        result = math_ops.square(4)
        if result == 16:
            print("Test PASS. The result of squaring 4 is correct.")
            print("Result:", result)
        else:
            print("Test FAIL. The result of squaring 4 is incorrect.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    print("=================================================================.")

    print("Test Case 3: Multiply two numbers.")
    print("=================================================================.")
    try:
        result = math_ops.multiply(3, 5)
        if result == 15:
            print("Test PASS. The result of multiplying 3 and 5 is correct.")
            print("Result:", result)
        else:
            print("Test FAIL. The result of multiplying 3 and 5 is incorrect.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    print("=================================================================.")

    print("Test Case 4: Power function.")
    print("=================================================================.")
    try:
        result = math_ops.power(2, 3)
        if result == 8:
            print("Test PASS. The result of 2 to the power of 3 is correct.")
            print("Result:", result)
        else:
            print("Test FAIL. The result of 2 to the power of 3 is incorrect.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    print("=================================================================.")

if __name__ == "__main__":
    main()
