player1 = [78, 43, 56, 65, 43, 45]
player2 = [54, 65, 87, 54, 56, 78]
player3 = [23, 65, 65, 43, 48, 54]
player4 = [54, 34, 67, 65, 43, 23]
scores = [player1, player2, player3, player4]
average_score = []


def calculate_average(pScore):
    total = 0
    for i in range(len(pScore)):
        total += pScore[i]
    return round(total / len(pScore), 3)


def display_player_stats(pScore):
    print("Score ({0} games) : {1}".format(len(pScore), pScore))
    print("Average Score: {0}".format(calculate_average(pScore)))
    print("Highest Score: {0}".format(max(pScore)))
    print("Lowest Score: {0}".format(min(pScore)))


def display_best_worst_player(average_score):
    print("-----------------------Best Performer of the Day-----------------------")
    print(
        "The best performer of the day is Player {0}".format(
            (average_score.index(max(average_score))) + 1
        )
    )
    print("The Player has an average score of {0}".format(max(average_score)))
    print("-----------------------Worst Performer of the Day-----------------------")
    print(
        "The worst performer of the day is Player {0}".format(
            (average_score.index(min(average_score))) + 1
        )
    )
    print("The Player has an average score of {0}".format(min(average_score)))


print("-----------------------Players Statistics-----------------------")
for i in range(len(scores)):
    print("Player {0}".format(i + 1))
    average_score.append(calculate_average(scores[i]))
    display_player_stats(scores[i])
display_best_worst_player(average_score)
