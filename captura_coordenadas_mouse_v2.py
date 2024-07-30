import os
import pyautogui

# Função para limpar a tela
def limpar_tela():
    # Limpa a tela no terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir as coordenadas do mouse sem parar
def exibir_coordenadas():
    while True:
        # Limpar a tela
        limpar_tela()
        # Obter as coordenadas do mouse
        x, y = pyautogui.position()
        # Exibir as coordenadas
        print('Coordenadas do Mouse: X =', x, 'Y =', y)

# Chamada da função
exibir_coordenadas()
