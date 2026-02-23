import random

moves = ("bato", "papel", "gunting")
isPlaying = True
isContinue = True

print("------------------ Welcome to TaraPik! ------------------")
print("This game is a simple rock(bato), paper(papel), scissor(gunting) game.\n"
      "You will choose your move while at the same time the computer chooses its own move.\n"
      "Remember this is a best of 5 game, goodluck!")
print("---------------------------------------------------------")

while isContinue:
    player_score = 0
    computer_score = 0

    while isPlaying:
        computer_move = random.choice(moves)
        player_move = None

        while player_move not in moves:
            player_move = input(f"\nChoose your move (bato, papel, gunting): ").lower().strip()

        print(f"\nYou picked: {player_move}. Computer picked: {computer_move}")
        if player_move == computer_move:
            print("Tie.")
        elif player_move == "bato" and computer_move == "gunting":
            print("You win!")
            player_score += 1
        elif player_move == "gunting" and computer_move == "papel":
            print("You win!")
            player_score += 1
        elif player_move == "papel" and computer_move == "bato":
            print("You win!")
            player_score += 1
        else:
            print("You lose")
            computer_score += 1
        print(f"Player Score: {player_score}\n"
              f"Computer Score: {computer_score}")

        if player_score == 3:
            print("\nCongratulations you win the game!")
            break
        elif computer_score == 3:
            print("\nBetter luck next time! :p")
            break
    if not input("Do you still want to continue?(y/n): ").lower().strip() == "y":
     isContinue = False