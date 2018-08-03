"""To guess the number used by user"""

HIGH = 100
LOW = 0
print("Please think of a number between 0 and 100!")
while True:
    GUESS = int((HIGH + LOW)//2)
    RESPONSE =  input("Is your secret number " + str(GUESS) + "? " + 
                    "Enter 'h' to indicate the guess is too high. " + 
                    "Enter 'l' to indicate the guess is too low. " + 
                    "Enter 'c' to indicate I guessed correctly. ")
    if RESPONSE == 'c':
        print("Game over. Your secret number was: " + str(GUESS))
        break
    elif RESPONSE == 'h':
        HIGH = GUESS
    elif RESPONSE == 'l':
        LOW = GUESS
    