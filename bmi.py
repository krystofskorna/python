# Body Mass Index
# Popis fungování programu (co a jak dělá)
# Ukázka použití: python bmi.py

# Uživatelské vstupy
height = float(input("Zadejte svou výšku v metrech:\n"))
weight = float(input("Zadejte svou váhu v kg:\n"))

# Výpočet BMI
bmi = weight / height **2 

# print(round(bmi , 1))

# Zhodnocení BMI
if bmi < 18.5 :
    print(f"Váš BMI má hodnotu {round(bmi , 1)}, máte podváhu")

elif bmi < 24.9 :
    print(f"Váš BMI má hodnotu {round(bmi , 1)}, jste v normálu")

elif bmi < 29.9 :
    print(f"Váš BMI má hodnotu {round(bmi , 1)}, máte nadváhu")

elif bmi < 34.9 :
    print(f"Váš BMI má hodnotu {round(bmi , 1)}, jste obézní")

else :
    print(f"Váš BMI má hodnotu {round(bmi , 1)}, máte extrémní obezitu")

# Výstpu
# FIXME
