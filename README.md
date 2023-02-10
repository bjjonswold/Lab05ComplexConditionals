# Lab05 Complex Conditionals

Operations Application Lab

In this lab, we will fill out two functions which will recommned what clothes we should wear that day based on the weather. Specifically, we will look at three factors--temperature, clouds in the sky, and wind--to determine our output/recommendation. For example, if it is 20 degrees Farenheit, cloudy, and there isn't much wind, we will recommend that the user wears winter clothes. A full list of each correct output will be put below.

# Step 1 -- Temperature Classification Function

Users will enter the exact temperatue (in Farenheit) which we will classify into three segments--HOT, FAIR, or COLD. This function will take in the temperatue (given as a number) and return a string of the three listed classification above. COLD will be defined as any temperature less than 40. FAIR will be defined as any temperature less than 75 (and 40 or above). HOT will be any temperature that is 75 or above. Example inputs and return values are shown below.

```python
temperatureClassification(39)
```

Returns: COLD

```python
temperatureClassification(40)
```

Returns: FAIR

```python
temperatureClassification(59)
```

Returns: FAIR

```python
temperatureClassification(118)
```

Returns: HOT

Notice the variable tempClass at the top of the weatherAnnouncer function. It calls the temperatureClassification function with the actual temperature provided as a parameter for weatherAnnouncer. Us the variable tempClass when further developing the weatherAnnouncer function.

# Step 2 -- Guide for Development

At this point, we've narrowed our temperature into three distinct categories. We will use a boolean named clearSkies for our cloudiness weather factor and another boolean named windy for our last weather factor. So, if the weather was 75, raining, and had strong wind gusts, our three weather factor variables would be 75, False, and True, respectively. If it was 20 degrees outside, cloudy, and no wind our variables would read 20, False, and False, respectively.

From this, we can determine that our program will read a total of 12 different weather patterns (3 temperature classifications * 2 cloudiness classifications * 2 wind classifications). In the next part of our program, we will make an output based on each of the 12 possible weather patterns.

Use the table below as a reference for the correct function return statement based on each weather pattern.

| temp | tempClass | clearSkies | windy | RETURN STATEMENT                                                 |
| ---- | --------- | ---------- | ----- | ---------------------------------------------------------------- |
| 102  | HOT       | True       | True  | Wear summer clothes today.                                       |
| 85   | HOT       | True       | False | Wear summer clothes today.                                       |
| 98   | HOT       | False      | True  | Wear summer clothes today, but bring a rain jacket just in case. |
| 76   | HOT       | False      | False | Wear summer clothes today, but bring an umbrella just in case.   |
| 73   | FAIR      | True       | True  | Wear a jacket today.                                             |
| 62   | FAIR      | True       | False | Wear whatever you would like today.                              |
| 55   | FAIR      | False      | True  | Wear a jacket today.                                             |
| 58   | FAIR      | False      | False | Wear a jacket today.                                             |
| 22   | COLD      | True       | True  | Wear winter gear today.                                          |
| 38   | COLD      | True       | False | Wear winter gear today.                                          |
| 18   | COLD      | False      | True  | Just stay inside today.                                          |
| 15   | COLD      | False      | False | Wear winter gear today.                                          |

# Step 3 -- Weather Announcer Function

You will see that the first two weather patterns in the table above have been coded for you. Continue to make if statements for the remaining 10 weather patterns and return the correct statement based on the table above.

# Step 4 (optional) -- Condense If Statements

You will notice there is a comment befrore the first if statement in the weatherAnnouncer function. This encourages you to find a way to combine the first two if statements into one if statement. The combined if statement will give the correct return statement for the two weather patterns that can pass the statement. Continue to do this for each weather pattern that returns the same return statement as another weather pattern.

For example, the 4 COLD temperatures have 2 unique return statements. Can you contain the 4 COLD temperatures into 2 unique if statements?

# Submitting the Assignment

Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Logical Operators

There are three logical operators. They are:

1) and
2) or
3) not

The 'and' logical operator is true if both sides of the statement are true. Otherwise the operator returns true. Below is an example using this logical operator.

```python
a = 20
b = 5
if a > 0 and b > 0:
    print('Both numbers are greater than 0')

if a > 10 and b > 10:
    print('Both numbers are greater than 10')
```

In this case, the first print statement will execute, but the second print statement won't execute.

The 'or' logical operator is true if either side of the statement is true. A similar example of this logical operator is shown below.

```python
a = 20
b = 5

if a > 0 and b > 0:
    print('At least one number is greater than 0')

if a > 10 and b > 10:
    print('At least one number is greater than 10')
```

Both of these print statements will execute.

The 'not' logical operator is true if the operand is false. In other words, this logical operator flips the operand it evaluates. Examples are shown below.

```python
a = True
b = False

if(not a):
    print('This statement will not execute')

if(not b):
    print('This statement will execute')
```

```python
c = 20
if not (c%7 == 0 or c%5 == 0): #     % gets the remainder
    print("20 is not divisible by either 7 or 5")
else:
    print("20 is divisible by either 7 or 5")
```

This outputs '20 is divisible by either 7 or 5'.
