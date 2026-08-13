import random
def play_game():
    lucky_num=random.randint(1,50)

    while True:
        user_num=int(input("Guess the number:"))

        if user_num==lucky_num:
            print("You won:thanks for playing")
            break
        elif user_num<lucky_num:
            print("Too Low")
        elif user_num>lucky_num:
            print("Too High")
        else:
            print("input out of range number:")
play_game()