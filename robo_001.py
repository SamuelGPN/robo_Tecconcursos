import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Encontrar o elemento que tem a rolagem (exemplo: uma div com lista)
bloco_scroll = browser.find_element(By.CLASS_NAME, "arvore-wrapper")

def rolar():
    # Rolar até o final do bloco
    last_height = browser.execute_script("return arguments[0].scrollHeight", bloco_scroll)

    while True:
        # Rola dentro do bloco
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bloco_scroll)
        time.sleep(2)  # Espera carregar mais itens

        new_height = browser.execute_script("return arguments[0].scrollHeight", bloco_scroll)
        if new_height == last_height:  # Se não carregar mais nada, parar
            break
        last_height = new_height

rolar()

browser.implicitly_wait(10)
materia_tipo = browser.find_elements(By.CLASS_NAME, 'arvore-item-icone-nome-wrap')

lista_cursos = list()
for n in materia_tipo:
    text = n.text

    print(text)
    print(n.accessible_name)
    print(n.tag_name)
    print(n.size)
    #print(n.shadow_root)
    print(n.screenshot_as_png)
    print(n.rect)
    print(n.parent)
    print(n.location_once_scrolled_into_view)
    print(n.location)
    print(n.screenshot_as_png)
    print(n.__class__)
    print(n.id)
    print(n.aria_role)


    if text == '':
        break
    lista_cursos.append(text)
    """
    else:
        n.click()

        materia_subtipo_pai = browser.find_elements(By.CLASS_NAME, 'arvore-item ng-scope ng-isolate-scope arvore-item-selecionar-tudo')
        for o in materia_subtipo_pai:
            materia_subtipo_filho = o.find_elements(By.CLASS_NAME, 'arvore-item-icone-nome-wrap')
            print(materia_subtipo_filho)
            for m in materia_subtipo_filho:
                print(m.text)

        n.click() #clique para fechar a pasta 
        rolar()

        time.sleep(1)
    """



browser.implicitly_wait(2)
pesquisa_element = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/span[2]/a')
pesquisa_element.click()

#for e in lista_cursos:



print(lista_cursos)


time.sleep(1)


time.sleep(100)

