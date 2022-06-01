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
        num = num * (-1)
    while(num == num):
        if num < 0:
            break
        else:
            total = total * num
            num = num - 1
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
