# Výpočet přestupných roků

# Proměnná
year = int(input("Zadejte rok :\n"))

# Podmínky + Výpočty
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print("Je to přestupový rok.")

        else :
            print("Není to přestupný rok.")    
    
    else :
        print("Je to přestupný rok.")


else :
    print("Není to přestupný rok.")

# Ukázka použití: python leap_years.py
