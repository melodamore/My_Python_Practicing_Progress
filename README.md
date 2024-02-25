### [**`ⲘⲈ𝓛ⲞⲆⲀⲘⲞꞄⲈ `**](http://melodamore.blogspot.com)
##  My Python Programming Practicing Progress - Beginner
######  Daniel Yohannes_ _**@melodamore**_ _everywhere!

### Learning Sources (_Books, Websites, and Videos_)

| Type    | Code   | Title                                                                                                                                                                                                        | Autor                |
|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Book    | `B001` | [**Python Basics**](https://terrorgum.com/tfox/books/pythonbasics_aselfteachingintroduction.pdf) **- A self-teaching Introduction**                                                                          | _H.Bhasin_           |
| Book    | `B002` | [**Beginning Python**](https://englishonlineclub.com/pdf/Beginning%20Python%20-%20From%20Novice%20to%20Professional%20%28Third%20Edition%29%20[EnglishOnlineClub.com].pdf) **- From Novice to Professional** | _Magnus Lie Hetland_ |
| Book    | `B003` | [**Fundamentals of Python**](https://vdoc.pub/download/fundamentals-of-python-from-first-programs-through-data-structures-41oa8209hfm0) **- From First Programs Through Data Structures**                    | _Kenneth A. Lambert_ |
| Book    | `B004` | [**Python Essential Reference**](https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Python/Python%20Essential%20Reference%2C%20Fourth%20Edition%20%282009%29.pdf) **- Developer's Library**          | _David M. Beazley_   |
| Book    | `B005` | [**Think Python**]() **- How to Think Like a Computer Scientist**                                                                                                                                            | _Allen Downey_       |
| Website | `W001` | [**Python.org**](https://www.python.org) **- Python Documentation**                                                                                                                                          | _Python_             |
| Website | `W002` | [**Microsoft.com**](https://learn.microsoft.com/en-us/training/browse/?terms=python) **- Introduction to Python**                                                                                            | _Microsoft_          |
| Website | `W003` | [**Tutorials Point**](https://www.tutorialspoint.com/python/index.htm)                                                                                                                                       | __                   |
| Website | `W004` | [**Udemy**]()                                                                                                                                                                                                |                      |
| Website | `W005` | [**W3 Schools**](https://www.w3schools.com/python/default.asp)                                                                                                                                               |                      |
| Video   | `V001` | [**Harvard CS50’s Introduction to Programming with Python**]() **- Full University Course**                                                                                                                  | _David J. Malan_     |   

___


| **Chapters**                                      |
|---------------------------------------------------|
| [Python Objects](#Python-Objects)                 |
| [Conditional Statements](#Conditional-Statements) |
| [Looping](#Looping)                               |

___
___

# `Python Objects`

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
- **Division** `/`
- **Power** **`**`** 
  - for exponentiation
- **Modulo** **`%`** 
  - finds the remained if the 1st number is greater, otherwise it returns the 1st number
- [**Example B001.0**](/Examples/Eg_B001.0_Operators.py)
___
## Some Important Functions of `math`
### Ceil
- The nearest integer `>=` the number
  - [**Example B001.1**](/Examples/Eg_B001.1_ceil.py)

### Copy sign
- The sign of the 2nd argument is returned
  - [**Example B001.2**](/Examples/Eg_B001.2_copy sign.py)

### Fabs
- Absolute value of a number
  - [**Example B001.3**](/Examples/Eg_B001.3_Fabs.py)

### Factorial
- The continued product of a number from 1 to that value
  - [**Example B001.4**](/Examples/Eg_B001.4_Factorial.py)

### Floor
- The nearest integer `<=` the number
  - [**Example B001.5**](/Examples/Eg_B001.5_Floor.py)
___
## Fractions
- From fractions import Fraction
- From decimal import Decimal
  - [**Example B001.6**](/Examples/Eg_B001.6_Fractions.py)
___
## Sequences
### Strings
- A predefined object which contains characters
- Non-mutable (Once defined, cannot be changed)

  - **Index**
    - A Particular location of a string
    - The index of the first location is 0
      - [**Example B001.7**](/Examples/Eg_B001.7_Indexing.py)
      
  - **Negative index**
    - The character present at the nth position beginning from the end
      - [**Example B001.8**](/Examples/Eg_B001.8_-ve_Indexing.py)
      
  - **Length**
    - Gives information about how many characters are found in a string
      - [**Example B001.9**](/Examples/Eg_B001.9_Length.py) 
      
  - **Concatenation**
     - adding strings using the operator `+`
       - [**Example B001.10**](/Examples/Eg_B001.10_Concatenation(+).py)
     - multiplying a string using the operator `*`
       - [**Example B001.11**](/Examples/Eg_B001.11_Concatenation(*).py)
       
  - **Slicing**
    - Removing some part of a string
      - [**Example B001.12**](/Examples/Eg_B001.12_Slicing.py)
  
### Lists `[]`
- A collection of objects 
- The most general sequence provided by the language 
- Mutable 
- A list can be a collection of similar elements (homogeneous)
- It can also contain different elements (heterogeneous)
- A list can also be empty `[]`
- A list can also contain a list 
- An element of a list can be accessed by indexing 
  - [**Example B001.13**](/Examples/Eg_B001.13_Lists.py)

### Tuples `()`
- Contains elements which can be treated individually or as a group 
- The elements of a tuple can be accessed by assigning it to a tuple 
- A tuple may also contain heterogeneous elements 
- Are extremely useful in operations like swapping 
  - [**Example B001.14**](/Examples/Eg_B001.14_Tuples.py)

### Problems
- `Problem #B001.2.1` Write a program to swap two numbers
  - [**Solution**](/Solutions/Sol_B001.1_Swap_Two_Numbers.py)


- `Problem #B001.2.2` Ask the user to enter the coordinates of a point and find the distance of the point from the origin.
  - [**Solution**](/Solutions/Sol_B001.2_Distance_Between_Point_&_Origin.py)


- `Problem #B001.2.3` Ask the user to enter two points (x and y coordinates) and find the distance between them.
  - [**Solution**](/Solutions/Sol_B001.3_Distance_Between_2_Points.py)


- `Problem #B001.2.4` Ask the user to enter three points and find whether they are collinear.
  - [**Solution**](/Solutions/Sol_B001.4_If_3_Points_Are_Collinear.py)


- `Problem #B001.2.5` In the above question, if the points are not collinear then find the type of triangle formed by them 
  (equilateral , isosceles or scalene).
  - [**Solution**](/Solutions/Sol_B001.5_Find_Type_of_Triangle.py)
 

- `Problem #B001.2.6` In the above question, check if the triangle is right-angled.
  - [**Solution**](/Solutions/Sol_B001.6_If_Triangle_is_Right_Angled.py)


- `Problem #B001.2.7` In question number 4, find the angles of the triangle.
  - [**Solution**](/Solutions/Sol_B001.7_Angle_of_Triangle.py)


- `Problem #B001.2.8` Ask the user to enter two points and find if they are at equal distances from the origin.
  - [**Solution**](/Solutions/Sol_B001.8_If_2_Points_are_Equidistant.py)


- `Problem #B001.2.9` In question number 8, find the angle between the line joining the points and the origin.
  - [**Solution**](/Solutions/Sol_B001.9_Angle_Between_Line_&_Origin.py) 


- `Problem #B001.2.10` Ask the user to enter 4 points and arrange them in order of their distances from the origin.
  - [**Solution**](/Solutions/Sol_B001.10_Arrange_4_Points_Based_on_Distance.py) 


- `Problem #B001.2.11` In question 10, arrange the above points in order of their x coordinates.
  - [**Solution**](/Solutions/Sol_B001.11_Arrange_4_Points_Based_on_X_Coordinates.py)

___
___
# `Conditional Statements`

## If-else
- Executed if the 'test' condition is true otherwise not executed
- indentation is important, as Python recognizes a block through indentation
  - [**Example**](/Examples/Eg_B001.15_If-else.py)


- **Important points**
    - The if <test> is followed by a colon.
    - There is no need of parentheses for this test condition. Though enclosing test in parentheses will not result 
      in an error.
    - The nested blocks in python are determined by indentation. Therefore, proper indentation in Python is essential. 
      As a matter of fact, an inconsistent indentation or no indentation will result in errors.
    - An `if` can have any number of if's nested within.
    - The test condition in `if` must result in a True or a False.
___
## The if-elif-else ladder

- To be used when there are multiple outcomes and the outcomes decide the action.
  - [**Example**](/Examples/Eg_B001.16_The_if-elif-else_Ladder.py)
___
## Logical Operators

  `and` or `&`  
  - The output is **true**, when both the conditions are **true**.
  - The truth table of `a` & `b`:

    | a   | b | a & b |
    |-----|---|-------|
    | T   | T | T     |
    | T   | F | F     |
    | F   | T | F     |
    | F   | F | F     |
     - [**Example**](/Examples/Eg_B001.17_Logical_Operators[and(&)].py)

  `or` or `|`  
  - The output is **true**, if any of the conditions are **true**.
  - The truth table of `a` & `b`:

    | a   | b | a or b |
    |-----|---|--------|
    | T   | T | T      |
    | T   | F | T      |
    | F   | T | T      |
    | F   | F | F      |
     - [**Example**](/Examples/Eg_B001.18_Logical_Operators%5Bor(%7C)%5D.py)
___
## The Ternary Operator

- The ternary operator performs the same task as the if-else construct.
- The problem is that each part caters to a single statement.
  - [**Example**](/Examples/Eg_B001.19_The_Ternary_Operator.py)
___

## The Get Construct
- [**Example**](/Examples/Eg_B001.20_The_Get_Construct.py)
___
## Illustrations
- **`Illustration #B001.3.1`** Ask the user to enter the marks of a student in a subject. If the marks entered are greater than 
  40 then print “pass,” if they are lower print “fail.”
  - [**Solution**](/Solutions/Sol_B001.12_If_a_Student_Pass_or_Fail.py)


- `Illustration #B001.3.2` Ask the user to enter a three-digit number. Call it 'num'. Find the number obtained by reversing 
  the order of the digits. Find the sum of the given number and that obtained by reversing the order of the digits. 
  Finally, find if any digit in the sum obtained is the same as that in the original number.
  - [**Solution**](/Solutions/Sol_B001.13_Sum_of_a_3_Digit_Number_And_Its_Reverse.py)
  

- `Illustration #B001.3.3` Write a program to find the greatest of the three numbers entered by the user.
  - [**Solution**](/Solutions/Sol_B001.14_Greatest_of_3_Numbers.py)


- `Illustration #B001.3.4` Find the greatest of the three numbers entered by the user using a ternary operator.
  - [**Solution**](/Solutions/Sol_B001.15_Greatest_of_3_Numbers_Using_Ternary_Operator.py)


- `Illustration #B001.3.5` Ask the user to enter a number and check whether its ASCII value is greater than 80.
  - [**Solution**](/Solutions/Sol_B001.16_If_ASCII_Greater_Than_80.py)


- `Illustration #B001.3.6` Ask the user to enter a number 'x' and if the number is greater than 2, calculate it with
  `f(x) = x^2 + 5X + 3` else calculate it with `f(X) = x + 3`
  - [**Solution**](/Solutions/Sol_B001.17_Calculate_X_With_2_Functions.py)


- `Illustration #B001.3.7` Ask the user to enter the coefficients of `a1x + b1y + c1 = 0` and `a2x + b2y + c2 = 0` and find out 
   whether the two lines depicted by the above equations are parallel or not.
  - [**Solution**](/Solutions/Sol_B001.18_If_2_Lines_Are_Parallel.py)


- `Illustration #B001.3.8` Ask the user to enter the values of `a1`,` a2`, `b1`,` b2`, `c1`, and `c2` and find whether the 
   lines are parallel, or if they  overlap or intersect.
  - [**Solution**](/Solutions/Sol_B001.19_If_2_Lines_Overlap_or_Intersect_or_Are_Parallel.py)
___
## Problems
- `Problem #B001.3.1` Ask the user to enter a number and find the number obtained by reversing the order of the digits.
  - [**Solution**](/Solutions/Sol_B001.20_Reverse_a_Number.py)


- `Problem #B001.3.2` Ask the user to enter a four-digit number and check whether the sum of the first and the last digits is 
   same as the sum of the second and the third digits.
  - [**Solution**](/Solutions/Sol_B001.21_If_Sum_of_a_4_Digit_Numbers_Are_Equal.py)


- `Problem #B001.3.3` In the above question if the answer is true then obtain a number in which the second and the third digit 
   are one  more than that in the given number. Example: Number 5342, sum of the first and the last digit = 7 that of 
   the second and the third digit = 7. New number: 5452
  - [**Solution**](/Solutions/Sol_B001.22_5342_to_5452.py)


- `Problem #B001.3.4` Ask the user to enter the concentration of hydrogen ions in a given solution (C) and find the PH of the 
   solution using the following formula. `PH = log10C`
  - [**Solution**](/Solutions/Sol_B001.23_Find_PH.py)


- `Problem #B001.3.5`. If the PH is <7 then the solution is deemed acidic, else it is deemed as basic. Find if the given 
   solution is acidic.
  - [**Solution**](/Solutions/Sol_B001.24_If_a_Solution_is_Acidic.py)
___
___

# `Looping`
___
###### Python provides two types of loops: `for` and `while`
___
## While
- For repeating a task over and over again
- The task is repeated until the test condition remains true
- The body of the loop is determined by indentation

## For

___
## Illustrations
- `Illustration #B001.4.1` Ask the user to enter a number and calculate its factorial
  - [**Solution**](/Solutions/Sol_B001.25_Calculate_Factorial.py)


- `Illustration #B001.4.2` Ask the user to enter two numbers `a` and `b` and calculate `a` to the power of `b`
  - [**Solution**](/Solutions/Sol_B001.26_Calculate_'a'_to_The_Power_of_'b'.py)


- `Illustration #B001.4.3` The arithmetic progression is obtained by adding the common difference `d` to the first term `a`, 
  successively. The ith term of the arithmetic progression is given by the following formula: `T(i) = a + (i - 1) * d`. 
  Ask the user to enter the value of `a`, `d` and `n` (the number of terms), and find all the terms of the AP. 
  Also, find the sum of all the terms. 
  - [**Solution**](/Solutions/Sol_B001.27_Arithmetic_Progression.py)


- `Illustration #B001.4.4` The geometric progression is obtained by multiplying the common ratio `r` to the first term `a`, 
   successively. The ith term of the progression is given by the following formula. `T(i) = a × ri – 1` Ask the user to 
   enter the value of `a`, `r`, and `n`(the number of terms), and find all the terms of the GP. 
   Also, find the sum of all the terms.
  - [**Solution**](/Solutions/Sol_B001.28_Geometric_Progression.py)