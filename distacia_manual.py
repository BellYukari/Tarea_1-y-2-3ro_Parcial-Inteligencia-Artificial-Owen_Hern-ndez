import cv2
import numpy as np
import math
import os

# Variables globales
puntos = []

# Función para manejar clics del mouse
def click_event(event, x, y, flags, param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(puntos) < 2:
            puntos.append((x, y))
            print(f"Punto seleccionado: ({x}, {y})")
            # Dibujar el punto
            cv2.circle(img_copy, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Selecciona dos puntos", img_copy)
            
            if len(puntos) == 2:
                # Calcular distancia en píxeles
                x1, y1 = puntos[0]
                x2, y2 = puntos[1]
                distancia_pixeles = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                # Conversión a centímetros (ajusta según tu escala)
                escala_cm_por_px = 0.05  # <-- AJUSTA ESTO SEGÚN TU IMAGEN
                distancia_cm = distancia_pixeles * escala_cm_por_px
                
                print(f"Distancia en píxeles: {distancia_pixeles:.2f}")
                print(f"Distancia en centímetros: {distancia_cm:.2f} cm")
                
                # Mostrar línea y texto
                cv2.line(img_copy, puntos[0], puntos[1], (255, 0, 0), 2)
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                cv2.putText(img_copy, f"{distancia_cm:.2f} cm", (mid_x, mid_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                cv2.imshow("Selecciona dos puntos", img_copy)
                
                # Guardar la imagen con los resultados
                cv2.imwrite("resultado_con_puntos.jpg", img_copy)
                
                # Guardar los resultados en un archivo .txt
                with open("resultados.txt", "w") as f:
                    f.write(f"Distancia en píxeles: {distancia_pixeles:.2f}\n")
                    f.write(f"Distancia en centímetros: {distancia_cm:.2f} cm\n")

# --- Inicio del programa ---
if __name__ == "__main__":
    # Ruta de la imagen (ajustar según tu caso)
    ruta_imagen = "circulos.jpg"  # Cambia por tu archivo: .jpg o .jpeg
    
    # Cargar imagen
    img = cv2.imread(ruta_imagen)
    if img is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        exit()

    # Crear copia para dibujar
    img_copy = img.copy()

    # Ventana para selección
    cv2.imshow("Selecciona dos puntos", img_copy)
    print("Haz clic en el centro de dos círculos.")
    print("Cierra la ventana cuando termines.")

    # Configurar el callback del mouse
    cv2.setMouseCallback("Selecciona dos puntos", click_event)

    # Esperar a que el usuario cierre la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()