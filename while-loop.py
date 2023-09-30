secret_number = 4
guess = int(input("Guess a number: "))
while secret_number != guess:
    guess = int(input("Guess a number: "))
else:
    print("Congratulations, you got it!")
