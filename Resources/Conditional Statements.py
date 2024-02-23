# Conditional Statements
"""
- If-else  # Executed of the 'test' condition is true otherwise not executed
           # indentation is important, as Python recognizes a block through indentation
    - For examples see Eg_B001.15_If-else.py

    --> Illustration #1 Ask the user to enter the marks of a student in a subject. If the marks entered are greater than
        40 then print “pass,” if they are lower print “fail.”
          - For solutions see soln_B001.12_If_a_Student_Pass_or_Fail.py

    --> Illustration #2 Ask the user to enter a three-digit number. Call it 'num'. Find the number obtained by reversing
        the order of the digits. Find the sum of the given number and that obtained by reversing the order of the digits
        Finally, find if any digit in the sum obtained is the same as that in the original number.
            - For solutions see solution13.py

    --> Important points  # The if <test> is followed by a colon.
                          # There is no need of parentheses for this test condition. Though enclosing test in
                            parentheses will not result in an error.
                          # The nested blocks in python are determined by indentation. Therefore, proper indentation in
                            Python is essential. As a matter of fact, an inconsistent indentation or no indentation will
                            result in errors.
                          # An 'if' can have any number od if's nested within.
                          # The test condition in 'if' must result in a True or a False.

    --> Illustration #3 Write a program to find the greatest of the three numbers entered by the user.
            - For solutions see solution14.py

- The if-elif-else ladder  # To be used when there are multiple outcomes and the outcomes decide the action
    - For examples see Eg_B001.16_The_if-elif-else_Ladder.py

- Logical Operators
    - 'and' ('&')  # The output is 'true', when both the conditions are 'true'.
                   # The truth table of 'a & b'
                         _______________________________
                        |___a___|_____b_____|___a & b__|
                        |   T   |     T     |     T    |
                        |   T   |     F     |     F    |
                        |   F   |     T     |     F    |
                        |___F___|_____F_____|_____F____|
                    - For examples see Eg_B001.17_Logical_Operators[and(&)].py

    - 'or' ('|')  # The output is 'true', if any of the conditions are 'true'.
                  # The truth table of 'a | b'
                        _______________________________
                        |___a___|_____b_____|___a & b__|
                        |   T   |     T     |     T    |
                        |   T   |     F     |     T    |
                        |   F   |     T     |     T    |
                        |___F___|_____F_____|_____F____|
                  - For examples see Eg_B001.18_Logical_Operators[or(|)].py

- The Ternary Operator  # The ternary operator performs the same task as the if-else construct.
                        # The problem is that each part caters to a single statement.
                            - For examples see Eg_B001.19_The_Ternary_Operator.py

    --> Illustration #4 Find the greatest of the three numbers entered by the user using a ternary operator.
            - For solutions see solution15.py

- The Get Construct
    - For examples see Eg_B001.20_The_Get_Construct.py

--> Illustration #5 Ask the user to enter a number and check whether its ASCII value is greater than 80.
        - For solutions see solution16.py

--> Illustration #6 Ask the user to enter a number 'x' and if the number is greater than 2, calculate it with
    'f(x) = x^2 + 5X + 3' else calculate it with 'f(X) = x + 3'
        - For solutions see solution17.py

--> Illustration #7 Ask the user to enter the coefficients of a1x + b1y + c1 = 0 and a2x + b2y + c2 = 0 and find out
    whether the two lines depicted by the above equations are parallel or not.
        - For solutions see solution18.py

--> Illustration #8 Ask the user to enter the values of a1, a2, b1, b2, c1, and c2 and find whether the lines are
    parallel, or if they overlap or intersect.
        - For solutions see solution19.py

Problems
    1. Ask the user to enter a number and find the number obtained by reversing the order of the digits.
        - For solutions see solution20.py

    2. Ask the user to enter a four-digit number and check whether the sum of the first and the last digits is same as
       the sum of the second and the third digits.
        - For solutions see solution21.py

    3. In the above question if the answer is true then obtain a number in which the second and the third digit are one
       more than that in the given number. Example: Number 5342, sum of the first and the last digit = 7 that of the
       second and the third digit = 7. New number: 5452
        - For solutions see solution22.py

    4. Ask the user to enter the concentration of hydrogen ions in a given solution (C) and find the PH of the solution
       using the following formula.
            PH = log10C
        - For solutions see solution23.py

    5. If the PH is <7 then the solution is deemed acidic, else it is deemed as basic. Find if the given solution is
       acidic.
        - Fo solutions see solution24.py
"""
