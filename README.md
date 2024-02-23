### [**`ⲘⲈ𝓛ⲞⲆⲀⲘⲞꞄⲈ `**](http://melodamore.blogspot.com)
######  Daniel Yohannes_ _**@melodamore**_ _everywhere!
### Learning Sources (_Books, Websites, and Videos_)

| Type | Code   | Title                                                                                                                                                                                                        | Autor                |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Book | `Boo1` | [**`Python Basics`**](https://terrorgum.com/tfox/books/pythonbasics_aselfteachingintroduction.pdf) **A self-teaching Introduction**                                                                          | _H.Bhasin_           |
| Book | `B002` | [**`Beginning Python`**](https://englishonlineclub.com/pdf/Beginning%20Python%20-%20From%20Novice%20to%20Professional%20%28Third%20Edition%29%20[EnglishOnlineClub.com].pdf) **From Novice to Professional** | _Magnus Lie Hetland_ |
| Book | `B003` | [**`Fundamentals of Python`**](https://vdoc.pub/download/fundamentals-of-python-from-first-programs-through-data-structures-41oa8209hfm0 **From First Programs Through Data Structures**                     | _Kenneth A. Lambert_ |
| Book | `B004` | [**`Python Essential Reference`**](https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Python/Python%20Essential%20Reference%2C%20Fourth%20Edition%20%282009%29.pdf) **Developer's Library**          | _David M. Beazley_   |


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
- **Power** **`**`** 
  - for exponentiation
- **Modulo** **`%`** 
  - finds the remained if the 1st number is greater, otherwise it returns the 1st number
- [**Example**]()
___
## Some Important Functions of `math`
### Ceil
- The nearest integer >= the number
  - [**Example**](/Examples/Eg_B001.1_ceil.py)

### Copy sign
- The sign of the 2nd argument is returned
  - [**Example**](/Examples/Eg_B001.2_copy sign.py)

### Fabs
- Absolute value of a number
  - [**Example**](/Examples/Eg_B001.3_Fabs.py)

### Factorial
- The continued product of a number from 1 to that value
  - [**Example**](/Examples/Eg_B001.4_Factorial.py)

### Floor
- The nearest integer <= the number
  - [**Example**](/Examples/Eg_B001.5_Floor.py)
___
## Fractions
- From fractions import Fraction
- From decimal import Decimal
  - [**Example**](/Examples/Eg_B001.6_Fractions.py)
___
## Sequences
### Strings
### Lists
### Tuples

### Problems
___
___
# `C-2 Conditional Statements`

## If-else
- Executed if the 'test' condition is true otherwise not executed
- indentation is important, as Python recognizes a block through indentation
  - [**Example**]()


- **Important points**
    - The if <test> is followed by a colon.
    - There is no need of parentheses for this test condition. Though enclosing test in parentheses will not result 
      in an error.
    - The nested blocks in python are determined by indentation. Therefore, proper indentation in Python is essential. 
      As a matter of fact, an inconsistent indentation or no indentation will result in errors.
    - An 'if' can have any number of if's nested within.
    - The test condition in 'if' must result in a True or a False.
___
## The if-elif-else ladder

- To be used when there are multiple outcomes and the outcomes decide the action.
  - [**Example**]()
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
     - [**Example**]()

  `or` or `|`  
  - The output is **true**, if any of the conditions are **true**.
  - The truth table of `a` & `b`:

    | a   | b | a or b |
    |-----|---|--------|
    | T   | T | T      |
    | T   | F | T      |
    | F   | T | T      |
    | F   | F | F      |
     - [**Example**]()
___
## The Ternary Operator

- The ternary operator performs the same task as the if-else construct.
- The problem is that each part caters to a single statement.
  - [**Example**]()
___

## The Get Construct
- [**Example**]()
___
## Illustrations
- **`Illustration #1`** Ask the user to enter the marks of a student in a subject. If the marks entered are greater than 
  40 then print “pass,” if they are lower print “fail.”
  - [**Solution**]()


- `Illustration #2` Ask the user to enter a three-digit number. Call it 'num'. Find the number obtained by reversing 
  the order of the digits. Find the sum of the given number and that obtained by reversing the order of the digits. 
  Finally, find if any digit in the sum obtained is the same as that in the original number.
  - [**Solution**]()
  

- `Illustration #3` Write a program to find the greatest of the three numbers entered by the user.
  - [**Solution**]()


- `Illustration #4` Find the greatest of the three numbers entered by the user using a ternary operator.
  - [**Solution**]()


- `Illustration #5` Ask the user to enter a number and check whether its ASCII value is greater than 80.
  - [**Solution**]()


- `Illustration #6` Ask the user to enter a number 'x' and if the number is greater than 2, calculate it with
  `f(x) = x^2 + 5X + 3` else calculate it with `f(X) = x + 3`
  - [**Solution**]()


- `Illustration #7` Ask the user to enter the coefficients of `a1x + b1y + c1 = 0` and `a2x + b2y + c2 = 0` and find out 
   whether the two lines depicted by the above equations are parallel or not.
  - [**Solution**]()


- `Illustration #8` Ask the user to enter the values of `a1`,` a2`, `b1`,` b2`, `c1`, and `c2` and find whether the 
   lines are parallel, or if they  overlap or intersect.
  - [**Solution**]()
___
## Problems
- `Problem #1` Ask the user to enter a number and find the number obtained by reversing the order of the digits.
  - [**Solution**]()


- `Problem #2` Ask the user to enter a four-digit number and check whether the sum of the first and the last digits is 
   same as the sum of the second and the third digits.
  - [**Solution**]()


- `Problem 3` In the above question if the answer is true then obtain a number in which the second and the third digit 
   are one  more than that in the given number. Example: Number 5342, sum of the first and the last digit = 7 that of 
   the second and the third digit = 7. New number: 5452
  - [**Solution**]()


- `Problem 4` Ask the user to enter the concentration of hydrogen ions in a given solution (C) and find the PH of the 
   solution using the following formula. `PH = log10C`
  - [**Solution**]()


- `Problem 5`. If the PH is <7 then the solution is deemed acidic, else it is deemed as basic. Find if the given 
   solution is acidic.
  - [**Solution**]()
___
___

# `C-3 Looping`
___
###### Python provides two types of loops: `for` and `while`
___
## While
- For repeating a task over and over again
- The task is repeated until the test condition remains true
- The body of the loop is determined by indentation

___
## Illustrations
- `Illustration #1` Ask the user to enter a number and calculate its factorial
  - [**Solution**](/Solutions/Sol_B001.25_Calculate_Factorial.py)


- `Illustration #2` Ask the user to enter two numbers `a` and `b` and calculate `a` to the power of `b`
  - [**Solution**](/Solutions/Sol_B001.26_Calculate_'a'_to_The_Power_of_'b'.py)


- `Illustration #3` The arithmetic progression is obtained by adding the common difference `d` to the first term `a`, 
  successively. The ith term of the arithmetic progression is given by the following formula: `T(i) = a + (i - 1) * d`. 
  Ask the user to enter the value of `a`, `d` and `n` (the number of terms), and find all the terms of the AP. 
  Also, find the sum of all the terms. 
  - [**Solution**](/Solutions/Sol_B001.27_Arithmetic_Progression.py)


- `Illustration #4` The geometric progression is obtained by multiplying the common ratio `r` to the first term `a`, 
   successively. The ith term of the progression is given by the following formula. `T(i) = a × ri – 1` Ask the user to 
   enter the value of `a`, `r`, and `n`(the number of terms), and find all the terms of the GP. 
   Also, find the sum of all the terms.
  - [**Solution**](/Solutions/Sol_B001.28_Geometric_Progression.py)