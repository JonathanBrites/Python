import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

try:
    # Inicialização do navegador
    navegador = webdriver.Chrome()
    navegador.maximize_window()
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

    # Espera implícita após o login
    navegador.implicitly_wait(10)

    # Clicar em relatório
    botao_relatorio = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/div[2]/div[4]/div[2]/small')
    botao_relatorio.click()

    # Clicar em operação
    botao_operacao = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[1]/div/aside/ul/li[2]/a')
    botao_operacao.click()

    # Clicar em ordens de serviço
    botao_ordens_servico = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[1]/div/aside/ul/li[2]/ul/li[3]/a')
    botao_ordens_servico.click()

    # Localize o elemento sobre o qual você deseja mover o mouse
    elemento_hover = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[11]/td[3]')

    # Mover o mouse para o elemento
    ActionChains(navegador).move_to_element(elemento_hover).perform()

    time.sleep(5)

    # Agora, o botão de download deve estar visível, você pode clicar nele
    botao_download = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[11]/td[4]/span/span/button/span/i')
    botao_download.click()

     # Executar um script JavaScript para obter o dia, mês e ano atual
    dia_atual = datetime.datetime.now().strftime("%d")
    mes_atual = datetime.datetime.now().strftime("%m")
    ano_atual = datetime.datetime.now().strftime("%Y")

    # Pressionar a tecla 'Tab' três vezes
    for _ in range(3):
        pyautogui.press('tab')
        # Inserir a data atual usando pyautogui
        pyautogui.typewrite('01')
        pyautogui.typewrite(mes_atual)
        pyautogui.typewrite(ano_atual)
        
    for _ in range(1):
        pyautogui.press('tab')
        # Inserir a data atual usando pyautogui
        pyautogui.typewrite(dia_atual)
        pyautogui.typewrite(mes_atual)
        pyautogui.typewrite(ano_atual)

    # Agora, o botão de download deve estar visível, você pode clicar nele
    botao_download = navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/footer/button[2]')
    botao_download.click()    

    # Espera para visualização
    time.sleep(220)

except Exception as e:
    print("Erro:", e)

finally:
    # Fechar o navegador
    navegador.quit()
