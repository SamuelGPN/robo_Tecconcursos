import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://www.tecconcursos.com.br/login')

browser.implicitly_wait(10)
email = browser.find_element(By.ID, 'email')
email.send_keys('leo.gcosta90@gmail.com')

browser.implicitly_wait(10)
email = browser.find_element(By.ID, 'senha')
email.send_keys('YgmXdKVl')

browser.implicitly_wait(10)
iframe = browser.find_element(By.TAG_NAME, "iframe")
browser.switch_to.frame(iframe)  # Entrar no iframe do reCAPTCHA
browser.implicitly_wait(10)
browser.find_element(By.CLASS_NAME, "recaptcha-checkbox").click()
# Voltar para o contexto principal
browser.switch_to.default_content()

try:
    browser.implicitly_wait(10)
    entrar_btn = browser.find_element(By.ID, 'entrar-site')
    entrar_btn.click()
except:
    time.sleep(15)

time.sleep(3)
browser.get('https://www.tecconcursos.com.br/questoes/cadernos/novo/')

time.sleep(1)

browser.implicitly_wait(5)
pesquisar_materia_btn = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/span[2]/a')
pesquisar_materia_btn.click()

browser.implicitly_wait(5)
pesquisar_materia = browser.find_element(By.XPATH,
                                         '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/span[1]/div/input')
pesquisar_materia.send_keys(Keys.CONTROL + 'a')
pesquisar_materia.send_keys(f'ADMINISTRACAO DE RECURSOS')
pesquisar_materia.send_keys(Keys.ENTER)

browser.implicitly_wait(5)
materia_tipo_geral_fixo = browser.find_element(By.XPATH,
                                               '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/div/span[2]')
materia_tipo_geral_fixo.click()                      #'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li'
time.sleep(3)

time.sleep(2)
sublista_element_1 = browser.find_elements(By.XPATH,
                                          '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li')


#sublista_element = sublista_element_1.find_elements(By.CLASS_NAME, 'arvore-item ng-scope ng-isolate-scope arvore-item-selecionar-tudo')
qtd_sublistas = len(sublista_element_1)
print(qtd_sublistas)