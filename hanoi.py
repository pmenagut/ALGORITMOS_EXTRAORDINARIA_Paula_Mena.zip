def hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi puzzle recursively.

    Parameters
    ----------
    n : int
        The number of disks.
    source : str
        The name of the source rod.
    target : str
        The name of the target rod.
    auxiliary : str
        The name of the auxiliary rod.

    Returns
    -------
    None
    """
    # Implementación de la función hanoi
    if n == 1:
        print(f"Mover disco 1 de {source} a {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Mover disco {n} de {source} a {target}")
        hanoi(n - 1, auxiliary, target, source)


def main():
    """Function main of the module.

    The function main of this module is used to test the function hanoi.

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
    from io import StringIO
    import sys

    def test_hanoi(n, source, target, auxiliary, expected_output):
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            hanoi(n, source, target, auxiliary)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            if output == expected_output.strip():
                print("Test PASS. The output is correct.")
            else:
                print("Test FAIL. The output is incorrect.")
        except Exception as e:
            sys.stdout = sys.__stdout__
            print(f"Test FAIL. {e}")

    print("=================================================================.")
    print("Test Case 1: Solve the Tower of Hanoi with 1 disk.")
    print("=================================================================.")
    expected_output_1 = "Mover disco 1 de A a C"
    test_hanoi(1, 'A', 'C', 'B', expected_output_1)
    print("=================================================================.")

    print("Test Case 2: Solve the Tower of Hanoi with 2 disks.")
    print("=================================================================.")
    expected_output_2 = "Mover disco 1 de A a B\nMover disco 2 de A a C\nMover disco 1 de B a C"
    test_hanoi(2, 'A', 'C', 'B', expected_output_2)
    print("=================================================================.")

    print("Test Case 3: Solve the Tower of Hanoi with 3 disks.")
    print("=================================================================.")
    expected_output_3 = (
        "Mover disco 1 de A a C\n"
        "Mover disco 2 de A a B\n"
        "Mover disco 1 de C a B\n"
        "Mover disco 3 de A a C\n"
        "Mover disco 1 de B a A\n"
        "Mover disco 2 de B a C\n"
        "Mover disco 1 de A a C"
    )
    test_hanoi(3, 'A', 'C', 'B', expected_output_3)
    print("=================================================================.")

    print("Test Case 4: Solve the Tower of Hanoi with 4 disks.")
    print("=================================================================.")
    expected_output_4 = (
        "Mover disco 1 de A a B\n"
        "Mover disco 2 de A a C\n"
        "Mover disco 1 de B a C\n"
        "Mover disco 3 de A a B\n"
        "Mover disco 1 de C a A\n"
        "Mover disco 2 de C a B\n"
        "Mover disco 1 de A a B\n"
        "Mover disco 4 de A a C\n"
        "Mover disco 1 de B a C\n"
        "Mover disco 2 de B a A\n"
        "Mover disco 1 de C a A\n"
        "Mover disco 3 de B a C\n"
        "Mover disco 1 de A a B\n"
        "Mover disco 2 de A a C\n"
        "Mover disco 1 de B a C"
    )
    test_hanoi(4, 'A', 'C', 'B', expected_output_4)
    print("=================================================================.")

if __name__ == "__main__":
    main()