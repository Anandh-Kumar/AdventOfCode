with open("2022/Day2/puzzle.txt") as f:
    rounds = f.readlines()
    win = {
        "A" : "Y",
        "B" : "Z",
        "C" : "X"
    }
    lose = {
        "A" : "Z",
        "B" : "X",
        "C" : "Y"
    }
    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    scores = {
        "X" :1,
        "Y" : 2,
        "Z": 3
    }
    total_score = 0
    for round in rounds:
        first_player = round.split()[0]
        prediction = round.split()[1]

        if prediction == "X":
            my_move = lose[first_player]
            total_score += scores[my_move]
        elif prediction == "Y":
            my_move = draw[first_player]
            total_score += scores[my_move] + 3
        else:
            my_move = win[first_player]
            total_score += scores[my_move] + 6
    print(total_score)