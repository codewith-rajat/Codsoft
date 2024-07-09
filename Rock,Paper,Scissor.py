import random
def game(b):
    c=["rock","paper","scissor"]
    d=random.choice(c)
    if (b=="rock" and d=="rock")or (b=="paper" and d=="paper") or(b=="scissor" and d=="scissor"):
        print("\nYour Choice:",b)
        print("Computer's Choice:",d)
        print("\nIt's a tie!!")
    elif (b=="paper" and d=="rock") or (b=="rock" and d=="scissor") or (b=="scissor" and d=="paper"):
        print("\nYour Choice:",b)
        print("Computer's Choice:",d)
        print("\nHurrah,You Won!!!")
    else:
        print("\nYour Choice:",b)
        print("Computer's Choice:",d)
        print("\nOh no,You Lose")
b=input("Choose from rock/paper/scissor:")
game(b)
while True:
    f=input("Do you want to play again?")
    if f=="yes":
        b=input("Choose from rock/paper/scissor:")
        game(b)
    else:
        break

