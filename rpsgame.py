import random
user_score = 0
computer_score = 0
rounds = 0
# welcome message
print("Welcome to Rock, Paper, and Scissors Online Game.")
name =  (input("what is your name?: "))
print(f"Hello {name}, ")
print("You are Player 1 and the Computer is Player 2."
"\nKindly make a choice from the available options, click enter to start game!")

game_options = ["Rock", "Paper", "Scissors"]
 
while True :
     rounds += 1
     user_1 = (input(f"{name}, Kindly make a choice (Rock, Paper, Scissors):   "))
     user_2 = random.choice(game_options)
     print(f"{name} chose {user_1} and computer chose {user_2}.")
     
     if user_1 == user_2:
        print("A Tie, Try again!")
     elif user_1 == "Rock" and user_2 == "Paper":
        computer_score += 1
        print("Computer wins, go again !!!")

     elif user_1 == "Rock" and user_2 == "Scissors":
        user_score += 1
        print(f"{name} wins, go again !!!")

     elif user_1 == "Paper" and user_2 == "Rock":
        user_score += 1
        print(f"{name} wins, go again !!!")

     elif user_1 == "Paper" and user_2 == "Scissors":
        computer_score += 1
        print("Computer wins, go again !!!")

     elif user_1 == "Scissors" and user_2 == "Rock":
        computer_score += 1
        print("Computer wins, go again !!!")

     elif user_1 == "Scissors" and user_2 == "Paper":
        user_score += 1
        print(f"{name} wins, go again !!!")
    
     play_again = (input("Do you want to keep playing? y/n: "))
     if play_again.upper() != "Y":
         break

if user_score > computer_score:
    print("Congratulations!!, you won the game")
else:
    print("Sorry, you lost")   

print("Goodbye")



 

