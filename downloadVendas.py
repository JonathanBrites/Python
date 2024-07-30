from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from datetime import datetime

try:
    # Inicialização do navegador
    navegador = webdriver.Chrome()
    navegador.get('https://air.sumicity.net.br/#/dashboard')

    # Preenchimento do campo de email
    campo_email = WebDriverWait(navegador, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/section/form/div/div/input'))
    )
    campo_email.send_keys('EMAIL DO COLABORADOR')

    # Clicar no botão para prosseguir (exemplo de XPath, substitua pelo correto)
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

    # Aguardar 5 segundos após o login
    time.sleep(5)

    # clicar em relatório
    botao_relatorio = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/div[2]/div[4]/div[2]/small')
    botao_relatorio.click()

    time.sleep(5)

    # Aguardar até que o link desejado esteja visível e clicável
    link_operacao = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/section/div[2]/div[1]/div/aside/ul/li[1]/ul/li[2]/a'))
    )
    link_operacao.click()

    time.sleep(5)

    # Encontrar o elemento onde o cursor do mouse deve passar para mostrar o botão de impressão
    elemento_acionador = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[5]/td[3]'))
    )

    # Movendo o cursor do mouse para o elemento acionador
    actions = ActionChains(navegador)
    actions.move_to_element(elemento_acionador).perform()

    link_operacao = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[5]/td[4]/span/span/button/span/i'))
    )
    link_operacao.click()

    time.sleep(5)

    # Obter a data atual e formatá-la
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Pressionar a tecla 'Tab' três vezes
    for _ in range(3):
        pyautogui.press('tab')
        # Inserir a data atual usando pyautogui
        pyautogui.write(data_atual)
    for _ in range(1):
        pyautogui.press('tab')
        # Inserir a data atual usando pyautogui
        pyautogui.write(data_atual)

    botao_intermediario2 = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/footer/button[2]/span[1]/i')
    botao_intermediario2.click()
    time.sleep(5)

    # Aguardar 35 segundos para o download iniciar
    time.sleep(45)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    navegador.quit()