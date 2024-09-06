import random

def get_choices() -> set:
    player_choice : str = input("Bir seçenek girin (taş, kağıt, makas): ")

    options : list = ["taş", "kağıt", "makas"]

    computer_choise = random.choice(options)
    choices : set = {
        "player": player_choice,
        "computer": computer_choise
    }

    return choices

def check_win(player, computer) -> str:
    # print("You chose " + player + ", computer chose" + computer)
    print(f"{player}'ı seçtin, {computer}'ı seçti.")

    if player == computer:
        return "Berabere!"
    elif player == "taş":
        if computer == "makas":
            return "Taş makası kırar! Kazandın!"
        else:
            return "Kağıt taşı sarar! Kaybettin."
        
    elif player == "kağıt":
        if computer == "taş":
            return "Kağıt taşı sarar! Kazandın!"
        else:
            return "Makas kağıdı keser! Kaybettin."
        
    elif player == "makas":
        if computer == "makas":
            return "Makas kağıdı keser! Kazandın!"
        else:
            return "Taş makası kırar! Kaybettin."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)