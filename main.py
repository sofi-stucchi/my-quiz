import random 
print("Welcome to rock paper scissors. Play three rounds")

things = ["rock", "paper", "scissors"]

with open ('results.txt','w') as results_file:

    for round in things:
        print("Choose: rock, paper, or scissors:")

        userinput = input()
        print(f"\nRound with user choosing: {userinput}")
  
        with open ('opponent.txt', 'r') as file:
            opponent = file.readlines()

            random_line_number = random.randint(0, len(opponent) - 1)
            random_choice = opponent[random_line_number].strip()
            print(f"Computer chooses: {random_choice}")

            if userinput=="rock" and random_choice == "scissors": 
                result="Congratulations!!! You win"
            elif userinput=="rock" and random_choice == "paper":
                result="Ups! Computer wins"
            elif userinput=="rock" and random_choice == "rock":
                result="Tie"
    
            elif userinput=="paper" and random_choice == "rock": 
                result="Congratulations!!! You win"
            elif userinput=="paper" and random_choice == "scissors":
                result="Ups! Computer wins"
            elif userinput=="paper" and random_choice == "paper": 
                result="Tie"

            elif userinput=="scissors" and random_choice == "paper": 
                result="Congratulations!!! You win"
            elif userinput=="scissors" and random_choice == "rock":
                result="Ups! Computer wins"
            else: 
                result="Tie"

            results_file.write(f"Round with user choosing {userinput} and computer choosing {random_choice}: {result}\n")
            print(result)