import random

def display_header():
    print("Taş Kağıt Makas oyununa hoş geldiniz!")
    print("Oyunu oynamak için, seçimlerinizi aşağıdaki şekilde belirtin:")
    print("0 - Taş")
    print("1 - Kağıt")
    print("2 - Makas")
    print("3 - Çıkış")

def get_player_choice():
    choice = input("Seçiminizi yapın (0-3): ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 3:
        choice = input("Lütfen geçerli bir seçim yapın (0-3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(0, 2)

def convert_to_choice(choice):
    if choice == 0:
        return "Taş"
    elif choice == 1:
        return "Kağıt"
    else:
        return "Makas"

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Berabere!"
    elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
        return "Tebrikler, kazandınız!"
    else:
        return "Maalesef kaybettiniz!"

def display_result(player_choice, computer_choice, result):
    print(f"Siz {convert_to_choice(player_choice)} seçtiniz.")
    print(f"Bilgisayar {convert_to_choice(computer_choice)} seçti.")
    print(result)

def play_game():
    display_header()
    player_choice = get_player_choice()
    while player_choice != 3:
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)
        player_choice = get_player_choice()
    print("Oyun bitti. Tekrar bekleriz!")

play_game()
