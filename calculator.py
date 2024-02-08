# Kalkulačka
# Popis Programu:
  # Zadáš dvě čísla a operaci a máš výsledek
import sys


def TestNumInput(inp):
    x = inp
    if  inp.isnumeric():
      print("OK")
      
      return int(x)
    
    else:
       TestNumInput(input("Zadejte opravdové číslo!\n"))

def calc(n1, n2, op):
    res = 0
    if op == "*" :
      res = n1 * n2
    elif op == "q":
        sys.exit(0)
    elif op == "/" :
        res = n1 / n2
    elif op == "+" :
        res = n1 + n2
    elif op == "-" :
        res = n1 - n2 
    else:
        print("Neplatná operace")
        return
    print(f"Výsledek operace:\n{res}")


while True  :
    print("------------------------------------")
# Uživatelské vstupy
    num1 = input("Zadejte číslo\n")
    num1 = TestNumInput(num1)
    print(f"num1: {num1}")
    op = input("Zadejte operaci - *, /, +, - nebo stiskne 'Q' pro ukončení\n")

    num2 = input("Zadejte druhé číslo\n")
    num2 = TestNumInput(num2)
    print(f"num2: {num2}")

    calc(num1, num2, op)
# Ukázka použití: python calculator.py
