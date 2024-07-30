import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Coordenadas do mouse: ({x}, {y})")
    time.sleep(1)  # Aguarda 1 segundo antes de capturar novamente as coordenadas
