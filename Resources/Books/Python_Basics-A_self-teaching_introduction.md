### [**`ⲘⲈ𝓛ⲞⲆⲀⲘⲞꞄⲈ `**](http://melodamore.blogspot.com)
######  Daniel Yohannes [_**`@melodamore`**_](https://linktr.ee/melodamore) everywhere!
#### [**`Python Basics`**](/Resources/Books/Python_Basics__A_Self_Teaching.pdf) - A self-teaching Introduction by _**H.Bhasin**_
###### Code for examples and solutions: `B001`
___

| Chapter | Title                                         | Chapter | Titles                               |       
|---------|-----------------------------------------------|---------|--------------------------------------|
| 1       | [Introduction to Python]()                    | 11      | [Inheritance]()                      |
| 2       | [Python Objects]()                            | 12      | [Operator Overloading]()             |
| 3       | [Conditional Statements]()                    | 13      | [Exception Handling]()               |
| 4       | [Looping]()                                   | 14      | [Introduction to Data Structures]()  |
| 5       | [Functions]()                                 | 15      | [Stacks and Queues]()                |
| 6       | [Iteration, Generators, and Comprehensions]() | 16      | [Linked Lists]()                     |
| 7       | [File Handling]()                             | 17      | [Binary Search Trees]()              |
| 8       | [Strings]()                                   | 18      | [Introduction to NUMPY]()            |  
| 9       | [Introduction to Object-Oriented Paradigm]()  | 19      | [Introduction to MATPLOTLIB]()       |
| 10      | [Classes and Objects]()                       | 20      | [Introduction to Image Processing]() |

## Basic Data Types

## Numbers
- **Integers**
  - Don't have any fractional parts

- **Floats**
  - Have fractional parts
- **Complexes**
  - Have real and imaginary parts
___  
## Operators Supported in Numbers
- **Addition** **`+`**
- **Subtraction**  **`-`**
- **Multiplication** **`*`**
- **Power** **`**`** 
  - for exponentiation
- **Modulo** **`%`** 
  - finds the remained if the 1st number is greater, otherwise it returns the 1st number
___
## Some Important Functions of 'math'
### Ceil
- The nearest integer >= the number
- For examples see [**Example 1**](/Examples/Eg_B001.1_ceil.py)

### Copy sign
- The sign of the 2nd argument is returned
- For examples see [**Example 2**](/Examples/Eg_B001.2_copy sign.py)

### Fabs
- Absolute value of a number
- For examples see [**Example 3**](/Examples/Eg_3_Fabs.py)

### Factorial
- The continued product of a number from 1 to that value
- For examples see [**Example 4**](/Examples/Eg_4_Factorial.py)

### Floor
- The nearest integer <= the number
- For examples see [**Example 5**](/Examples/Eg_5_Floor.py)
___
## Fractions
- From fractions import Fraction
- From decimal import Decimal
- For examples see [**Example 6**](/Examples/Eg_6_Fractions.py)
___
### Sequences 
  - ### Strings
  - ### Lists
  - ### Tuples

### Problems
    
## C-2 Conditional Statements
    
### If-else

    - Executed if the 'test' condition is true otherwise not executed
    - indentation is important, as Python recognizes a block through indentation
        - For examples see example15.py

    - Illustration #1 Ask the user to enter the marks of a student in a subject. If the marks entered are greater than 
      40 then print “pass,” if they are lower print “fail.”
        - For solutions see solution12.py

    - Illustration #2 Ask the user to enter a three-digit number. Call it 'num'. Find the number obtained by reversing 
      the order of the digits. Find the sum of the given number and that obtained by reversing the order of the digits. 
      Finally, find if any digit in the sum obtained is the same as that in the original number.
            - For solutions see solution13.py

    - Important points
        - The if <test> is followed by a colon.
        - There is no need of parentheses for this test condition. Though enclosing test in parentheses will not result 
          in an error.
        - The nested blocks in python are determined by indentation. Therefore, proper indentation in Python is essential. 
          As a matter of fact, an inconsistent indentation or no indentation will result in errors.
        - An 'if' can have any number of if's nested within.
        - The test condition in 'if' must result in a True or a False.

    - Illustration #3 Write a program to find the greatest of the three numbers entered by the user.
        - For solutions see solution14.py

### The if-elif-else ladder

    - To be used when there are multiple outcomes and the outcomes decide the action.
        - For examples see example16.py

### Logical Operators

    - 'and' ('&')  # The output is 'true', when both the conditions are 'true'.
                   # The truth table of 'a & b'
                         _______________________________
                        |___a___|_____b_____|___a & b__|
                        |   T   |     T     |     T    |
                        |   T   |     F     |     F    |
                        |   F   |     T     |     F    |
                        |___F___|_____F_____|_____F____|
                    - For examples see example17.py

    - 'or' ('|')  # The output is 'true', if any of the conditions are 'true'.
                  # The truth table of 'a | b'
                        _______________________________
                        |___a___|_____b_____|___a & b__|
                        |   T   |     T     |     T    |
                        |   T   |     F     |     T    |
                        |   F   |     T     |     T    |
                        |___F___|_____F_____|_____F____|
                  - For examples see example18.py

### The Ternary Operator

    - The ternary operator performs the same task as the if-else construct.
    - The problem is that each part caters to a single statement.
        - For examples see example19.py

    - Illustration #4 Find the greatest of the three numbers entered by the user using a ternary operator.
        - For solutions see solution15.py

### The Get Construct
    
    - For examples see example20.py

### Illustration #5
    - Ask the user to enter a number and check whether its ASCII value is greater than 80.
        - For solutions see solution16.py

### Illustration #6
    - Ask the user to enter a number 'x' and if the number is greater than 2, calculate it with 'f(x) = x^2 + 5X + 3' 
      else calculate it with 'f(X) = x + 3'
        - For solutions see solution17.py
[solution17.py]()
### Illustration #7
    - Ask the user to enter the coefficients of a1x + b1y + c1 = 0 and a2x + b2y + c2 = 0 and find out whether the two 
      lines depicted by the above equations are parallel or not.
        - For solutions see solution18.py

### Illustration #8
    - Ask the user to enter the values of a1, a2, b1, b2, c1, and c2 and find whether the lines are parallel, or if they
      overlap or intersect.
        - For solutions see solution19.py

### Problems
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

## C-3 Looping

#### Python provides two types of loops: `for` and `while`

### While
- For repeating a task over and over again
- The task is repeated until the test condition remains true
- The body of the loop is determined by indentation

### Illustration #1

- Ask the user to enter a number and calculate its factorial
- For solutions see [**Solution 25**](/Solutions/solution25.py)

### Illustration #2

- Ask the user to enter two numbers `a` and `b` and calculate `a` to the power of `b`
- For solutions see [**Solution 26**](/Solutions/solution26.py)

### Illustration #3

- The arithmetic progression is obtained by adding the common difference `d` to the first term `a`, successively. The 
  ith term of the arithmetic progression is given by the following formula: `T(i) = a + (i - 1) * d`.  
  Ask the user to enter the value of `a`, `d` and `n` (the number of terms), and find all the terms of the AP. 
  Also, find the sum of all the terms. 
- For solutions see [**Solution 27**](/Solutions/solution27.py)