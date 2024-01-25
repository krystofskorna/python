# Body Mass Index
# Popis fungování programu (co a jak dělá)
    #Vyjede tam věta "Zadejte svou výšku v metrech:" a vy zadáte výšku v metrech např. 1.8
    #Potom tam zadáte svoji váhu a výjde vám jak jste na tom.
# Uživatelské vstupy
height = float(input("Zadejte svou výšku v metrech:\n"))
weight = float(input("Zadejte svou váhu v kg:\n"))

# Výpočet BMI
bmi = weight / height **2 

# Zhodnocení BMI
if bmi < 16.5 :
    x = " těžkou podvýživu"

elif bmi < 18.5 :
    x = " podváhu"

elif bmi < 25 :
    x = " ideální váhu"

elif bmi < 29.9 :
    x = " nadváhu"

elif bmi < 34.9 :
    x = " obezitu 1. stupně"

elif bmi < 40 :
    x = " obezitu 2. stupně"

else :
    x = " obezitu 3. stupně"

print("Máte" +  x )

# Ukázka použití: python bmi.py
