from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from datetime import datetime

try:
    # Inicialização do navegador e maximizar a janela
    navegador = webdriver.Edge()
    navegador.maximize_window()  # Maximiza a janela do navegador
    navegador.get('https://alloha.fs.ocs.oraclecloud.com/')

    # Preenchimento do campo de email
    campo_email = WebDriverWait(navegador, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    campo_email.send_keys('EMAIL DO COLABORADOR')
    time.sleep(2)

    # Preenchimento do campo de senha
    campo_senha = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    campo_senha.send_keys('SENHA DO COLABORADOR')
    time.sleep(2)

    # Clicar no botão de login
    botao_login = navegador.find_element(By.XPATH, '//*[@id="second-step-container"]/div[5]')
    botao_login.click()

    # Esperar até que a página seja carregada após o login
    time.sleep(10)

    # Clique no botão de alguma ação específica (substitua pelos valores corretos)
    pyautogui.click(x=1150, y=240, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

    # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=977, y=373, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

    # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=963, y=407, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

     # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=966, y=444, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

     # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=966, y=467, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

    # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=1145, y=587, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

    # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=1262, y=221, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(2)

    # Clique no próximo botão (substitua pelos valores corretos)
    pyautogui.click(x=1215, y=321, duration=0.5)

    # Esperar até que alguma outra ação seja completada
    time.sleep(35)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    navegador.quit()
