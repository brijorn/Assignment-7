from TrviaQns import create_trivia_questions

def ask_question(question, player):
    print(f'Question for the {player} player:')
    print(question)
    player_answer = int(input("Enter your solution (a number 1 between and 4): "))
    if player_answer == question.correct_answer_num:
        print("That is the correct answer.\n")
        return True
    else:
        print("That is incorrect. The correct answer is", question.correct_answer_num, "\n")
        return False



def main():
    questions = create_trivia_questions()

    turn = 1
    player_1_points = 0
    player_2_points = 0
    while turn <= 10:
        player = "second" if turn % 2 == 0 else "first"

        # turn does not start at zero
        current_question = questions[turn-1]

        # Asks question and returns True if answer was correct.
        correct = ask_question(current_question, player)

        if player == "first" and correct:
            player_1_points += 1
        if player == "second" and correct:
            player_2_points += 1
        turn += 1

    print(f'The first player earned {player_1_points} points.')
    print(f'The second player earned {player_2_points} points.')
    if player_1_points > player_2_points:
        print("The first player win the game.")
    elif player_2_points > player_1_points:
        print("The second player win the game.")
    else:
        print("There was a tie!")
main()