import random

def repeat(get,start,end):
    if n == "yes" :
        print("You Want to Enter the range then type yes")
        m=input()
        if m == "yes":
            print("Enter the range")
            start=int(input())
            end=int(input())
            guess_the_number(start,end);
        else:
            guess_the_number(a,b);
    else :
        print ("Thank You For Playing Game")


def guess_the_number(start,end):
    guess=random.randint(start,end)

    for i in range(1,7):
        print("You have {} attpmet".format(7-i))
        user=int(input("Enter a number "))
        if user<guess:
            print("Your number is less than excepted value")
        if user>guess:
            print("Your number is greater than excepted value")
        if user==guess:
            print(" You won the game")
            break
    if user==guess:
        pass
    else:
        print(" You lost the game")
        print("Value is {}".format(g))
    print("If You Want to Play the Game again the enter yes ")
    get=input()
    repeat(get,start,end)

print("let start the GUESSING  game")
print("Enter the range")
start=int(input())
end=int(input())
guess_the_number(start,end)
