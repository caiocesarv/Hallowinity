# Importa o módulo webdriver do Selenium para controlar o navegador
from selenium import webdriver

# Importa WebDriverWait para fazer esperas dinâmicas (aguarda até certo elemento estar disponível)
from selenium.webdriver.support.ui import WebDriverWait

# Importa condições esperadas que usamos com WebDriverWait (como "elemento estar clicável")
from selenium.webdriver.support import expected_conditions as EC

# Importa a classe By, usada para indicar como selecionar um elemento (por ID, XPATH, etc.)
from selenium.webdriver.common.by import By

# Importa o módulo time, para fazer pausas com time.sleep()
import time

# Inicia o navegador Chrome
navegador = webdriver.Chrome()

# Abre o site do formulário de testes
navegador.get("https://formy-project.herokuapp.com/form")

# Coloca o navegador em modo de tela cheia
navegador.maximize_window()

# ----------- Preenchimento do formulário -----------

# Digita "Caio" no campo de primeiro nome (first name)
navegador.find_element(By.ID, "first-name").send_keys("Caio")

# Digita "César" no campo de sobrenome (last name)
navegador.find_element(By.ID, "last-name").send_keys("César")

# Digita "Desenvolvedor" no campo de título profissional (job title)
navegador.find_element(By.ID, "job-title").send_keys("Desenvolvedor")

# Seleciona a segunda opção de botão de rádio (radio button)
navegador.find_element(By.ID, "radio-button-2").click()

# Marca o primeiro checkbox da página
navegador.find_element(By.ID, "checkbox-1").click()

# ----------- Seleção de um item no dropdown -----------

# Encontra o menu suspenso (dropdown) e clica para abrir
dropdown = navegador.find_element(By.ID, "select-menu")
dropdown.click()

# Seleciona a opção de valor 2 (por exemplo: "College")
opcao = navegador.find_element(By.XPATH, "//option[@value='2']")
opcao.click()

# ----------- Preenchimento de data -----------

# Preenche o campo de data com "07/19/2025"
navegador.find_element(By.ID, "datepicker").send_keys("07/19/2025")

# ----------- Envio do formulário -----------

# Localiza o botão "Submit" usando XPath (baseado no texto do botão)
botao_enviar = navegador.find_element(By.XPATH, "//a[contains(text(), 'Submit')]")

# Faz scroll automático até o botão ficar visível na tela (centralizado)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_enviar)

# Cria uma espera de até 10 segundos para garantir que o botão esteja clicável
espera = WebDriverWait(navegador, 10)
espera.until(EC.element_to_be_clickable(botao_enviar))

# Clica no botão para enviar o formulário
botao_enviar.click()

# Espera 5 segundos para o usuário ver a próxima tela (ou mensagem de sucesso)
time.sleep(5)

# Fecha o navegador e encerra o programa
navegador.quit()