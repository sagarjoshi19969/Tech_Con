import random
WORDS = ("python", "java", "niit", "difficult", "answer", "apple")
print(
"""
           Welcome to NIIT's Jumble Word Game!

"""
)
point=10
play=1
count=0
while play==1:
    word = random.choice(WORDS)
    correct = word

    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("The jumble is:", jumble)
    ans=1
    while ans==1:
            if(count<5):
                guess = input("\nYour guess: ")

                if guess!=correct:
                    print("Result: Incorrect !! Better luck next time")
                    point=point-2
                    ans=1
                    count=count+1
                else:
                    print("Correct Answer")
                    print("Your score is ",point)
                    ans=0
                    play=int(input("Do you want to continue ? if yes the enter 1"))
            else:
                ans=0
                play=int(input("Your 5 attempts have exhausted \n Press 1 to continue"))


print("Thank You for Visiting Us")


