# Python Objects
"""
- Basic Data Types
    - Numbers
        - Integers #don't have any fractional parts
        - Floats #have fractional parts
        - Complexes #have real and imaginary parts

        --> OPERATORS SUPPORTED IN NUMBERS
            - Addition '+'
            - Subtraction '-'
            - Multiplication '*'
            - Power '**'  # for exponentiation
            - Modulo '%'  # finds the remained if the 1st number is greater, otherwise it returns the 1st number

        --> SOME IMPORTANT FUNCTIONS OF 'math'
            - Ceil  # The nearest integer >= the number
                - For examples see 'Eg_B001.1_ceil.py'
            - Copy sign  # The sign of the 2nd argument is returned
                - For example see 'Eg_B001.2_copy sign.py'
            - Fabs  # Absolute value of a number
                - For examples see 'Eg_3_Fabs.py'
            - Factorial  # The continued product of a number from 1 to that value.
                - For examples see 'Eg_4_Factorial.py'
            - Floor  # The nearest integer <= the number
                - For examples see 'Eg_5_Floor.py'

        --> FRACTIONS
                - From fractions import Fraction
                - From  decimal import Decimal
                    - For examples see 'Eg_6_Fractions.py'

    - Sequences
        - Strings  # A predefined object which contains characters
                    # Non-mutable (Once defined, cannot be changed)

            - Index  # A Particular location of a string
                     # The index of the first location is 0
                - For examples see 'Eg_7_Indexing.py'

            - Negative index  # The character present at the nth position beginning from the end
                - For examples see 'Eg_8_-ve_Indexing.py'

            - Length  # Gives info. about how many characters are found in a string
                - For examples see 'Eg_9_Length.py'

            - Concatenation  # adding strings using the operator '+'
                - For examples see 'Eg_10_Concatenation(+).py'
                            # multiplying a string using the operator '*'
                - For examples see 'Eg_11_Concatenation(*).py'

            - Slicing  # Removing some part of a string
                - For examples see 'Eg_12_Slicing.py'

        - Lists  # A collection of objects
                # The most general sequence provided by the language
                # Mutable
                # A list can be a collection of similar elements (homogeneous)
                # It can also contain different elements (heterogeneous)
                # A list can also be empty ([])
                # A list can also contain a list
                # An element of a list can be accessed by indexing
                    - For examples see 'Eg_13_Lists.py'

        - Tuples  # Contains elements which can be treated individually or as a group
                  # The elements of a tuple can be accessed by assigning it to a tuple
                  # A tuple may also contain heterogeneous elements
                  # Are extremely useful in operations like swapping
                    - For examples see 'Eg_14_Tuples.py'

- Problems
    1. Write a program to swap two numbers.
        - For solutions see solution1.py

    2. Ask the user to enter the coordinates of a point and find the distance of the point from the origin.
        - For solutions see solution2.py

    3. Ask the user to enter two points (x and y coordinates) and find the distance between them.
        - For solutions see solution3.py

    4. Ask the user to enter three points and find whether they are collinear.
        - For solutions see solution4.py

    5. In the above question, if the points are not collinear then find the type of triangle formed by them (equilateral
       , isosceles or scalene).
        - For solutions see solution5.py

    6. In the above question, check if the triangle is right-angled.
        - For solutions see solution6.py

    7. In question number 4, find the angles of the triangle.
        - For solutions see solution7.py

    8. Ask the user to enter two points and find if they are at equal distances from the origin.
        - For solutions see solution8.py

    9.
        - For solutions see solution9.py

    10. Ask the user to enter 4 points and arrange them in order of their distances from the origin.
        - For solutions see solution10.py

    11. In question 10, arrange the above points in order of their x coordinates.
        - For solutions see solution11.py
"""