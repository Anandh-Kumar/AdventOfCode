with open("2022/Day2/puzzle.txt") as f:
    rounds = f.readlines()
    scores = {
        "X" :1,
        "Y" : 2,
        "Z": 3
    }
    matches = {
        "AX" : 3,
        "BY" : 3,
        "CZ" : 3,
        "CX" : 6, 
        "BZ" : 6,
        "AY" : 6
    }
    total_score = 0
    for round in rounds:
        first_player = round.split()[0]
        second_player = round.split()[1]
        
        total_score += scores[second_player]
        total_score += matches.get(first_player + second_player, 0)
    
    print(total_score)
