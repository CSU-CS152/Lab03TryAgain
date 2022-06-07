# Lab03TryAgain
Loops and if warmup lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One

Read the following code in the attached file and answer the questions about it:
1. How does onlyOneRightAnswer work?
2. How many times does notAFactorial(9) loop?
3. There are two things wrong with notAFactorial. What should we change about it to make it properly produce a factorial?
4. How could we edit askForInput() to make it loop forever? (there are multiple correct answers)
5. How long does the actual while loop for notAFactorial run, when ignoring what happens inside of it? (how long does while(num == num) run?
7. Add a while loop to main to prompt the user for another num to give to magic8 until the user enters -1


# Step Two: Coding: magic8(num)
Find the function magic8(num). 

Write magic8(num) so that it uses num to predict an outcome. It must follow the following rules and return the appropriate strings
If num is less than 23, return "ask again later"
If num is 41, return "all signs point to yes"
If num is less than or equal to 72, return "outlook not so good"
Otherwise, return "concentrate and ask again"

For example, if someone calls the function with

magic8(-4) the function would return "ask again later"
magic8(70) the function would return "outlook not so good"
The function itself will not print or take in input from the client! Remember that when we want to write out a whole message, we usually use strings.

# Step 3: Test magic8(num)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().

print("TESTING", magic8(-4))
print("TESTING", magic8(70))
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on if statements


# Reminder on loops
