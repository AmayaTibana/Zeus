#We are importing the random module that we need to be able to generate random numbers
import random                      

#We are creating a random even number between 2 and 10 by 
#first randomizing a number between 1 and 5. This will be our
#final number. The number to add will take that and multiply it by 2.
numberToGuess = random.randrange(1, 5)
print('The random number generated is: ', numberToGuess) 
numberToAdd = numberToGuess * 2

#Asking the user to enter in their name
name = input("Hello! What is your name? ")

#Script to walk through each of the steps
print("Welcome " +name +", we’ll perform some mind reading on you.")

enteredNumber = int(input("Enter in a number between 1 and 10: "))

print("Multiply the result by 2.")

#userNumber = enteredNumber * 2
#print(">> userNumber at this step = " + str(userNumber))

answer = input("Ready for the next step? ")
print("Now, add...let's see...")
print('The number to add is: ', numberToAdd)

#userNumber = userNumber + numberToAdd
#print(">> userNumber at this step = " + str(userNumber))

answer = input("Ready for the next step? ")
print("Now, divide the number have by 2.")

answer = input("Ready for the next step? ")

#userNumber = userNumber / 2
#print(">> userNumber at this step = " + str(userNumber))

print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? ")

#Guessing the number
print("Well " +name +", let me read your mind...The number that you have right now a....")
print(numberToGuess)

#userNumber = userNumber - enteredNumber
#print(">> userNumber at this step = " + str(userNumber)