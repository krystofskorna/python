# Detekce okrajů

import cv2

# inicializace objektů pro stream z kamery
video = cv2.VideoCapture(0)

while True:
    # načtení snímku z kamery
    success, img = video.read()
    if success == True: # overeni uspesneho ziskani snimku z kamery
        # prevedení snímku do stupňu šedi
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # pužití algoritmu Canny pro detekci hran
        edges = cv2.Canny(gray, 80, 160)
        # Zobrazeni vysledku
        cv2.imshow('Demo - Edge Detection', edges)
        #cv2.imshow('Demo - Grey senzor', gray)
        #cv2.imshow('Demo - Colorful senzor', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# uvolnění prostředků a ukončení programu
video.release()
cv2.destroyAllWindows()
