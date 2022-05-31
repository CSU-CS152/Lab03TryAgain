# Lab03TryAgain
Loops and if warmup lab

Read the following code and answer the questions about it

#input: question–a string with a prompting question, correctAnswer–the correct input
#output: asks the user to try again if answer was incorrect or moves on if correct
def onlyOneRightAnswer(question, correctAnswer):
    while(input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")

#input: num–an int of some kind
#output: the positive factorial of num
def notAFactorial(num): #there are 2 things wrong with this--how do we fix it to make it return the factorial?
    total = 0
    if num < 0:
        num *= -1
    while(num == num):
        if num < 0:
            break
        else:
            total *= num
            num -= 1
    return total

#input: none
#output: prints the factorials of numbers given to it
def askForInput():
    while(input("Would you like to go again? y/n \n") != "n"):
        num = int(input("Give me a number! \n"))
        fact = notAFactorial(num)
        print("The factorial of " + str(num) + " is " + str(fact))
    print("\nGoodbye!!")

def main():
    askForInput()
    onlyOneRightAnswer("Would you like your fortune read?y/n\n ", "y")
    fortuneNum = int(input("Great! Give me your luckiest number from 0-100!\n"))
    magic8(fortuneNum) #you will write this one!


if __name__ == "__main__":
    main()



How does onlyOneRightAnswer work?

How many times does notAFactorial(9) loop?

There are two things wrong with notAFactorial. What should we change about it to make it properly produce a factorial?

How could we edit askForInput() to make it loop forever? (there are multiple correct answers)

How long does the actual while loop for notAFactorial run, when ignoring what happens inside of it? (how long does while(num == num) run?

Your turn. Write magic8(num) so that it uses num to predict an outcome. It must follow the following rules and return the appropriate strings

If num is less than 23, return “ask again later”
If num is 41, return “all signs point to yes”
If num is less than or equal to 72, return “outlook not so good”
Otherwise, return “concentrate and ask again”

Add a while loop to main to prompt the user for another num to give to magic8 until the user enters -1
