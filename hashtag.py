# Importar los módulos necesarios para la ejecución del programa.
from enum import Enum

class Hashtag(Enum):
    """Enum for the hashtags of the posts.

    This class defines the possible hashtags for the posts.
    """
    TRAVEL = "TRAVEL"
    FOOD = "FOOD"
    FASHION = "FASHION"
    TECHNOLOGY = "TECHNOLOGY"

def main():
    """Function main of the module.

    The function main of this module is used to test the Class HASHTAG.

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

    print("=================================================================.")
    print("Test Case 1: Check Class Hastag - Name.")
    print("=================================================================.")

    if isinstance(Hashtag.TRAVEL, Hashtag):
        print("Test PASS. The enum for TRAVEL has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Hashtag.FOOD, Hashtag):
        print("Test PASS. The enum for FOOD has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Hashtag.FASHION, Hashtag):
        print("Test PASS. The enum for FASHION has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(Hashtag.TECHNOLOGY, Hashtag):
        print("Test PASS. The enum for TECHNOLOGY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
