from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

try:
    # Inicialização do navegador
    navegador = webdriver.Chrome()
    navegador.maximize_window()  # Maximiza a janela do navegador
    navegador.get('https://air.sumicity.net.br/#/dashboard')

    # Preenchimento do campo de email
    campo_email = WebDriverWait(navegador, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/section/form/div/div/input'))
    )
    campo_email.send_keys('EMAIL DO COLABORADOR')

    # Clicar no botão para prosseguir
    botao_prosseguir = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/section/form/button/span[2]')
    botao_prosseguir.click()

    # Esperar até que o campo de senha seja visível
    campo_senha = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/form/div/div/input'))
    )
    campo_senha.send_keys('SENHA DO COLABORADOR')

    # Clicar no botão de login
    botao_login = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/form/button')
    botao_login.click()

    # Aguardar 10 segundos após o login
    time.sleep(8)

    # Clicar em "relatório"
    botao_relatorio = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/div[2]/div[4]/div[2]/small')
    botao_relatorio.click()

    time.sleep(15)

    # Clicar em "Operação"
    botao_operacao = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[1]/div/aside/ul/li[2]/a')
    botao_operacao.click()

    time.sleep(5)

    # Clicar em "Chamados"
    botao_ordens = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[1]/div/aside/ul/li[2]/ul/li[1]/a')
    botao_ordens.click()

    time.sleep(5)

      # Clicar em "Segunda Página"
    botao_ordens = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/a[2]/span/i')
    botao_ordens.click()

    time.sleep(5)

    # Localize o elemento sobre o qual você deseja mover o mouse
    elemento_hover = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[13]/td[3]')

    # Mover o mouse para o elemento
    ActionChains(navegador).move_to_element(elemento_hover).perform()

    time.sleep(5)

    # Agora, o botão de download deve estar visível, você pode clicar nele
    botao_download = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[13]/td[4]/span/span/button/span/i')
    botao_download.click()

    time.sleep(400)

finally:
    # Fechar o navegador
    navegador.quit()    