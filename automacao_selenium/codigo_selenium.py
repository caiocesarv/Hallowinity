from selenium import webdriver
import time

# abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://www.hashtagtreinamentos.com/")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar um elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde")

# clicar em um elemento
botao_verde.click()

# encontrar varios elementos
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

# selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# navegar para um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# escrever em um campo/formulario
navegador.find_element("id", "firstname").send_keys("Lira")
navegador.find_element("id", "email").send_keys("pythonimpressionador@gmail.com")
navegador.find_element("id", "phone").send_keys("2199999999")

botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

# dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         botao_quero_clicar)

# opcao 1 - espera manual
# time.sleep(3)

# opcao 2 - espera dinâmica
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()
time.sleep(10)