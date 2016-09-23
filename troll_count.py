"""
Problem:

    Many non-trolls stereotypically assume that trolls are illiterate
    and innumerate.

    This, like many stereotypes, is untrue.

    Trolls count like so:  one, two, many, lots ...

    Where "many" is any number between 3 and 8, and "lots" is any number
    bigger than 8. The troll_count function takes an integer in, and should
    print the appropriate troll equivalent.

Tests:
    >>> troll_count(1)
    one
    >>> troll_count(2)
    two
    >>> troll_count(3)
    many
    >>> troll_count(5)
    many
    >>> troll_count(8)
    many
    >>> troll_count(9)
    lots
    >>> troll_count(12)
    lots
"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this function:
def troll_count(n):

    if n > 8:
        print("That is a LOTS!")

    elif n < 1:
        print("None")

    elif n == 1:
        print("One")

    elif n == 2:
        print("Two")

    else:
        print("Many Troll Here!")
