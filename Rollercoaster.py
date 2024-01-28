# Horská dráha

# Popis programu:
        # Na začátku program vypíše větu tam zadáš výšku v cm 
        # Odpoví vám jestli můžete jet na zdráze
        # Následuje otázka ohledně věku kvůli ceně lístku 
        # Potom otázka na vyfocení při jízdě

# Uvítací věta
print("Vítejte na horské dráze ")

# Uživatelské vstupy
height = int(input("Jaká je vaše výška v cm?\n"))
bill = 0

# Podmínky a sčítání
if height >= 87 :
    print("Můžete jet na horské dráze.")
    
    age = int(input("Jaký je váš věk?\n"))
       
    if age <= 12 :
        bill += 50
        print("Cena vašeho lístku je 50 Kč")

    elif age >= 12 and age <= 18 :
        bill += 100
        print("Cena vašeho lístku je 100 Kč")
    
    elif age >= 40 and age <= 50:
        bill = 0
    else :
        bill += 150
        print("Cena vašeho lístku je 150 Kč")
    
    # Fotka při jízdě
    photo = input("Chcete během jízdy vyfotit?  ano nebo ne\n")

    if photo == "ano" :
        bill += 40
    
    print(f"Vaše cena je {bill} Kč")


else :
    print("Omlouváme se , ale na horské dráze jet nemůžete")

# Ukázka použití: python Rollercoaster.py
