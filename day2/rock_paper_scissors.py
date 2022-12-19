# The winner of the whole tournament is the player with the highest score. 
# Your total score is the sum of your scores for each round. The score for 
# a single round is the score for the shape you selected (1 for Rock, 2 for Paper,
# and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

#A and X = rock
# B and Y = paper
# C and X = scissors
# PART 1: total_score from the strategy guide assuming the above three lines

f = open('input.txt','r')
contents = f.readlines()
total_score= 0
for line in contents:
    round_score = 0
    my_choice = line[2]
    opponent_choice = line[0]
    if my_choice == 'X':
        round_score += 1
        if opponent_choice == 'A':
            round_score += 3
        elif opponent_choice == 'B':
            round_score += 0
        else:
            round_score += 6
    elif my_choice == 'Y':
        round_score += 2
        if opponent_choice == 'A':
            round_score += 6
        elif opponent_choice == 'B':
            round_score += 3
        else:
            round_score += 0
    else:
        # you chose scissors
        round_score += 3
        if opponent_choice == 'A':
            round_score += 0
        elif opponent_choice == 'B':
            round_score += 6
        else:
            round_score += 3
    total_score += round_score
print(total_score)
f.close()

# PART 2
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
# rock is 1 point, paper is 2 points, scissors is 3 points
f = open('input.txt','r')
contents = f.readlines()
total_score= 0
for line in contents:
    round_score = 0
    outcome = line[2]
    opponent_choice = line[0]
    if opponent_choice == 'A':
        if outcome == 'X':
            round_score = 3
        elif outcome == 'Y':
            round_score = 4
        else:
            round_score = 8
    elif outcome == 'Y':
        round_score += 2
        if opponent_choice == 'A':
            round_score += 6
        elif opponent_choice == 'B':
            round_score += 3
        else:
            round_score += 0
    else:
        # you chose scissors
        round_score += 3
        if opponent_choice == 'A':
            round_score += 0
        elif opponent_choice == 'B':
            round_score += 6
        else:
            round_score += 3
    total_score += round_score
print(total_score)
f.close()