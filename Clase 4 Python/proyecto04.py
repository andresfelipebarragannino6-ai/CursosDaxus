import cv2
from cvzone.HandTrackingModule import HandDetector

# 1. Configuramos la cámara
webcam = cv2.VideoCapture(0)

# 2. Definimos el ancho y alto
webcam.set(3, 853) 
webcam.set(4, 480)  

rastreador = HandDetector(detectionCon=0.8, maxHands=2)

if not webcam.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print("Cámara iniciada. Las coordenadas se mostrarán en la terminal.")

while True:
    exito, imagen = webcam.read()

    if not exito or imagen is None:
        break

    # Detectar manos
    manos, imagen = rastreador.findHands(imagen)

    # 3. Imprimir coordenadas si se detectan manos
    if manos:
        for i, mano in enumerate(manos):
            # lmList contiene los 21 puntos (x, y, z)
            puntos = mano["lmList"] 
            centro = mano["center"] # Centro de la mano (x, y)
            tipo = mano["type"]     # Izquierda o Derecha
            
            print(f"Mano {i+1} ({tipo}) - Centro: {centro}")
            # Ejemplo: Imprimir solo la punta del dedo índice (punto 8)
            print(f"Coordenada Dedo Índice (Punto 8): {puntos[8]}")
            print("-" * 30)

    # Mostramos la imagen
    cv2.imshow("Proyecto 4 - IA", imagen)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()