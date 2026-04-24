# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[], play_order={}):
    # Track opponent history
    if prev_play != "":
        opponent_history.append(prev_play)

    # Initialize play_order dictionary once
    if not play_order:
        plays = ["R", "P", "S"]
        for p1 in plays:
            for p2 in plays:
                play_order[p1 + p2] = 0

    # Default move
    guess = "R"

    # Build pattern tracking (last 2 moves → next move)
    if len(opponent_history) > 2:
        last_two = "".join(opponent_history[-2:])

        if last_two in play_order:
            play_order[last_two] += 1

        # Predict next move based on most frequent pattern
        potential = {
            last_two[1] + "R": play_order.get(last_two[1] + "R", 0),
            last_two[1] + "P": play_order.get(last_two[1] + "P", 0),
            last_two[1] + "S": play_order.get(last_two[1] + "S", 0),
        }

        prediction = max(potential, key=potential.get)[-1]

        # Counter the prediction
        counter = {"R": "P", "P": "S", "S": "R"}
        guess = counter[prediction]

    else:
        # Early game: random play
        guess = random.choice(["R", "P", "S"])

    return guess
