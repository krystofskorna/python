# Kámen, nůžky, papír
# Popis fungování programu:
    # Program bude požadovat číslo 1-3 aby jste si vybral co chcete zahrát
    # Potom program náhodně vygeneruje kámen, nůžky nebo papír

# Vložení modulu random
import random

# Proměnné
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_list =[rock, paper, scissors]


# Vstup uživatele
user_choose = int(input("Co si vyberete? Napište 0 pro kámen, 1 pro papír 2 pro nůžky\n"))                                                                                                                                                                                                                             

user_picture = all_list[user_choose]

computer_choose = random.randint(0, 2)

computer_picture = all_list[computer_choose]


print(f"Uživatel si vybral:\n {user_picture}")

print(f"Počítač náhodně vygeneroval:\n {computer_picture}")

# Ukázka použití: python rock_paper_scissors.py
