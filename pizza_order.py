# Aplikace na objednání pizzy

# Popis fungování programu:
    # Program se vás zeptá na velikost, extra sýr a šunku
    # Potom vyhodnotí celkovou částku k zaplacení

# Úvod
print("Vítejte v aplikaci na objednání pizzy")

# Proměnné 
size = input("Jakou chcete velikost pizzy? S, M, nebo L\n")

ham = input("Dáte si šunku navíc za 20 Kč S a za 30 Kč M, L? ano nebo ne\n")

cheese = input("Dáte si extra sýr za 15 Kč? ano nebo ne\n")

bill = 0

# Podmínky
if size == "S":
    bill += 100
    if ham == "ano":
        bill += 20
        if cheese == "ano":
            bill += 15    


elif size == "M" :
    bill += 150
    if ham == "ano":
        bill += 30
        if cheese == "ano":
            bill += 15



elif size == "L" :
    bill += 200
    if ham == "ano":
        bill += 30
        if cheese == "ano":
            bill += 15

# Celková částka
print(f"Částka k zaplacení : {bill} Kč")

# Úkázka použití: python pizza_order.py
