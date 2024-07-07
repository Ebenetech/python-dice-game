import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll 

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The players range: 2-4")
    else:
        print("Invalid input, Please try again")

#print(players)

max_score = 50
player_scores = [0 for _ in range(players)]
#print(player_scores)

while max(player_scores) < max_score:
    
    
    for player_index in range(players):
        print("\nPlayer number ", player_index + 1, "turn has just began\n")
        print("Your total score is: ", player_scores[player_index], "\n")
        recent_scores = 0
        
        
        while True:
            would_roll = input("Would you like to roll? (y)")
            if would_roll != "y":
                break
            
            value = roll()
            
            if value == 1:
                print("You rolled 1!, You are done👍")
                recent_scores = 0
                break
            else:
                recent_scores += value
                print("You rolled a: ", value)
            
            print("Your current score is: ", recent_scores)
        
        player_scores[player_index] += recent_scores
        print("Your Total score is: ", player_scores[player_index])    
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with the score of: ", max_score)