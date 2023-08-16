import random
a=input("Enter your name: ")
b=int(input("Choose any one of these \n1.Animals \n2.Birds \n3.States \n4.Districts \n"))

def get_world(b):
    
    if(b==1):
        data=open('pythonfullst\Hello.txt','r') 
        b=data.read().splitlines()
        abc=random.choice(b)
        return abc
    elif(b==2):
        data=open('birds.txt','r')
        b=data.read().splitlines()
        abc=random.choice(b)
        return abc
    elif(b==3):
        data=open('states.txt','r')
        b=data.read().splitlines()
        abc=random.choice(b)
        return abc
    elif(b==4):
        data=open('district.txt','r')
        b=data.read().splitlines()
        abc=random.choice(b)
        return abc
    else:
        print("Please select the correct choice")

    
guessword=get_world(b)
for i in guessword:
    print('*',end='')

length=len(guessword)
print("\nWord has %d letters" %length)    

def comparision(guessword,your_word):
    status=''
    for letter in guessword:
        if letter in your_word:
            status += letter
        else:
            status +='*'
    return status




def game_fun():
    points = 0
    guess = 0
    guessed = False
    your_word = []
    turns = len(guessword) + 1
    turns1 = turns

    print("Total turns: ", turns)
    while guess < turns1:
        guess1= input("Enter your Guess: ")
        turns -= 1
        print("Turns left ", turns)

        if guess1 in your_word:
            print("You already guessed")
        elif len(guess1) ==1:
            your_word.append(guess1)
            result = comparision(guessword,your_word)
            if result == guessword:
                guessed == True
                print("You Won "+ a)
                print("Word is "+ guessword)
                points += 10 
                turns1=0
            else:
                print(result)
               
        else:
            print("Invalid Entry")
        guess +=1
    if guess == turns1:
        print("Sorry You Lost the Game")
        print("Word id :",guessword)

    return points

game_points = game_fun()
print("Game Points :", game_points)



    



    

