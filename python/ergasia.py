import random

player_wins = 0
pc_wins = 0

while True:
    player_choice = input("Rock, paper or scissors? ").lower()
    pc_choice = random.choice(['rock', 'paper', 'scissors'])

    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Παρακαλώ , επιλέξτε ανάμεσα σε πέτρα,ψαλίδι ή χαρτί.")
        continue

    print("Η επιλογή σας :", player_choice + " Ο υπολογιστής επέλεξε :", pc_choice)

    if player_choice == pc_choice:
        print("Ισοπαλία!")
    elif (player_choice == 'rock' and pc_choice == 'scissors') or \
            (player_choice == 'paper' and pc_choice == 'rock') or \
            (player_choice == 'scissors' and pc_choice == 'paper'):
        print("Νίκησες!")
        player_wins += 1
    else:
        print("Ο υπολογιστής νίκησε!")
        pc_wins += 1

    play_again = input("Θέλετε να ξαναπαίξετε? (Yes/No): ").lower()
    if play_again != 'yes':
        print("Τελικό σκορ - Παίχτης:", player_wins, "Pc:", pc_wins)
        break