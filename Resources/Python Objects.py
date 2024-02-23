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
                - For examples see 'Eg_B001.3_Fabs.py'
            - Factorial  # The continued product of a number from 1 to that value.
                - For examples see 'Eg_B001.4_Factorial.py'
            - Floor  # The nearest integer <= the number
                - For examples see 'Eg_B001.5_Floor.py'

        --> FRACTIONS
                - From fractions import Fraction
                - From  decimal import Decimal
                    - For examples see 'Eg_B001.6_Fractions.py'

    - Sequences
        - Strings  # A predefined object which contains characters
                    # Non-mutable (Once defined, cannot be changed)

            - Index  # A Particular location of a string
                     # The index of the first location is 0
                - For examples see 'Eg_B001.7_Indexing.py'

            - Negative index  # The character present at the nth position beginning from the end
                - For examples see 'Eg_B001.8_-ve_Indexing.py'

            - Length  # Gives info. about how many characters are found in a string
                - For examples see 'Eg_B001.9_Length.py'

            - Concatenation  # adding strings using the operator '+'
                - For examples see 'Eg_B001.10_Concatenation(+).py'
                            # multiplying a string using the operator '*'
                - For examples see 'Eg_B001.11_Concatenation(*).py'

            - Slicing  # Removing some part of a string
                - For examples see 'Eg_B001.12_Slicing.py'

        - Lists  # A collection of objects
                # The most general sequence provided by the language
                # Mutable
                # A list can be a collection of similar elements (homogeneous)
                # It can also contain different elements (heterogeneous)
                # A list can also be empty ([])
                # A list can also contain a list
                # An element of a list can be accessed by indexing
                    - For examples see 'Eg_B001.13_Lists.py'

        - Tuples  # Contains elements which can be treated individually or as a group
                  # The elements of a tuple can be accessed by assigning it to a tuple
                  # A tuple may also contain heterogeneous elements
                  # Are extremely useful in operations like swapping
                    - For examples see 'Eg_B001.14_Tuples.py'

- Problems
    1. Write a program to swap two numbers.
        - For solutions see Sol_B001.1_Swap_Two_Numbers.py

    2. Ask the user to enter the coordinates of a point and find the distance of the point from the origin.
        - For solutions see Sol_B001.2_Distance_Between_Point_&_Origin.py

    3. Ask the user to enter two points (x and y coordinates) and find the distance between them.
        - For solutions see Sol_B001.3_Distance_Between_2_Points.py

    4. Ask the user to enter three points and find whether they are collinear.
        - For solutions see Sol_B001.3_If_3_Points_Are_Collinear.py

    5. In the above question, if the points are not collinear then find the type of triangle formed by them (equilateral
       , isosceles or scalene).
        - For solutions see Sol_B001.5_Find_Type_of_Triangle.py

    6. In the above question, check if the triangle is right-angled.
        - For solutions see soln_B001.6_If_Triangle_is_Right_Angled.py

    7. In question number 4, find the angles of the triangle.
        - For solutions see solution7.py

    8. Ask the user to enter two points and find if they are at equal distances from the origin.
        - For solutions see soln_B001.8_If_2_Points_are_Equidistant.py

    9.
        - For solutions see solution9.py

    10. Ask the user to enter 4 points and arrange them in order of their distances from the origin.
        - For solutions see soln_B001.10_Arrange_4_Points_Based_on_Distance.py

    11. In question 10, arrange the above points in order of their x coordinates.
        - For solutions see soln_B001.11_Arrange_4_Points_Based_on_X_Coordinates.py
"""