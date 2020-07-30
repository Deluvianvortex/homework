
# Purpose: Rock Paper Scissors game using dictionaries and nested loops

# first we define a dict() cypher so we can easily find what 'knocks' what
cypher = {'scissor':'rock',
          'rock':'paper',
          'paper':'scissor'}

# we need a choices list for the computer to choose from:
choices = ['rock','paper','scissor']


# this is effectively the start of the game, where we import and declare:
import random

gamenum = 1

tally = {}
games = {}
rounds = 0
n = 0
c = 0
p = 0
gameloop = 0
winner = ""

# with variables declared, we can get to using them in the actual loop:
while gameloop == 0:
    # the game will run twice no matter what:
    while n < 2:
        print("Game", gamenum)
        print("Round", rounds)
        pchoice = input("Enter your choice >").lower()

        compchoice = choices[random.randrange(3)]

        print("player choice is: ", pchoice)
        print("Comp choice is: ", compchoice)

        if pchoice == compchoice:
            print("Tie!")
            winner = "Tie"
        elif cypher[pchoice] == compchoice:
            print("You Lose!")
            c=c+1
            winner = "Computer"
        elif cypher[pchoice] != compchoice:
            print("You Win!")
            p=p+1
            winner = "Human"
        print("You have won {} rounds!".format(p))
        print("The Comp has won {} rounds!".format(c))
        
        rounds += 1
   
        tally[rounds] = winner
   
        if (p == 2) or (c == 2):
            n+=2
        games[gamenum] = tally
        # ask the player if they would like to play again:
    gameq = input("Would you like to play another game?(y/n):").lower()
    if gameq == "n":
        # if no, break the loop
        gameloop = 1
    else:
        #if yes, reset the vars
        gamenum += 1
        n = 0
        c = 0
        p = 0
        rounds = 0
        tally = {}
# display the game results:        
print("number of games:", gamenum)

for k in range (1, gamenum+1):
    print("Game:", k)
    for i in range (1, len(games[k])+1):
        print("Round {}: Winner: {}".format(i, games[k][i]))

print("Thanks for playing Rock Paper Scissors!")
