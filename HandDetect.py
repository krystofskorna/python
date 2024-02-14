import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector

WindowName = "Muj detektor hlavy a prstu"

# Inicializace objektů pro detektor ruky
detectorHand = HandDetector(maxHands=1, detectionCon=0.8)
detectorFace = FaceMeshDetector(maxFaces=10)
video = cv2.VideoCapture(0)
  
while True:
    success, img = video.read()
    if success == True:
    

        # Zrcadlové otočení snímku
        #img = cv2.flip(img, 1) 

        # Create a named window
        #cv2.namedWindow(WindowName, cv2.WND_PROP_FULLSCREEN)

        # Nastavit na fullscreen
        #cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        img, faces = detectorFace.findFaceMesh(img)   

        if faces:
            #print(faces[0]) # x, y pozice bodu na obliceji vypsane
            # Pokus o nalezení ruky ve snimku
            hand, img = detectorHand.findHands(img, draw=True)
            if hand:
                # Ulození informace o zvednutých prstech
                fingerup = detectorHand.fingersUp(hand[0])
                for finger in fingerup:
                    if finger == 1 :
                        finger = 'Zvednut'
                    else:
                        finger = "Nezvednut"
                cv2.putText(img, f'Palec: {fingerup[0]}', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                cv2.putText(img, f'Ukazovacek: {fingerup[1]}', (10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                cv2.putText(img, f'Prostrednicek: {fingerup[2]}', (10, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                cv2.putText(img, f'Prstenicek: {fingerup[3]}', (10, 120), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                cv2.putText(img, f'Malicek: {fingerup[4]}', (10, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                print(fingerup)
            else:
                cv2.putText(img, 'Nevidim ruku', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))

        cv2.imshow(WindowName, img)   

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
