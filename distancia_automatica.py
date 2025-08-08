import cv2
import numpy as np
import math

# Cargar imagen
img = cv2.imread('circulos1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_copy = img.copy()

# Detección de círculos
circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
    param1=50, param2=30, minRadius=10, maxRadius=100
)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    print(f"Se detectaron {len(circles)} círculos.")
    
    # Tomar los dos primeros círculos
    if len(circles) >= 2:
        (x1, y1, r1) = circles[0]
        (x2, y2, r2) = circles[1]
        
        # Dibujar círculos
        cv2.circle(img_copy, (x1, y1), r1, (0, 255, 0), 2)
        cv2.circle(img_copy, (x1, y1), 3, (0, 0, 255), -1)
        cv2.circle(img_copy, (x2, y2), r2, (0, 255, 0), 2)
        cv2.circle(img_copy, (x2, y2), 3, (0, 0, 255), -1)
        
        # Calcular distancia
        distancia_pixeles = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
        escala_cm_por_px = 0.05  # Ajustar
        distancia_cm = distancia_pixeles * escala_cm_por_px
        
        # Dibujar línea y texto
        cv2.line(img_copy, (x1, y1), (x2, y2), (255, 0, 0), 2)
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        cv2.putText(img_copy, f"{distancia_cm:.2f} cm", (mid_x, mid_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        print(f"Distancia: {distancia_cm:.2f} cm")
    else:
        print("No hay suficientes círculos detectados.")
else:
    print("No se detectaron círculos.")