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


# Gerar o xpath automaticamente:
def pegar_xpath(elemento):
    xpath1 = browser.execute_script("""
    function getElementXPath(element) {
        if (element.id !== '') {
            return '//*[@id="' + element.id + '"]';
        }
        if (element === document.body) {
            return element.tagName.toLowerCase();
        }

        let index = 1;
        let siblings = element.parentNode.children;
        for (let i = 0; i < siblings.length; i++) {
            if (siblings[i] === element) {
                return getElementXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + index + ']';
            }
            if (siblings[i].tagName === element.tagName) {
                index++;
            }
        }
    }
    return getElementXPath(arguments[0]);
    """, elemento)
    return xpath1

browser.implicitly_wait(10)
materia_tipo_geral = browser.find_elements(By.CLASS_NAME, 'arvore-item-icone-nome-wrap')

lista_cursos = list()
for n in materia_tipo_geral:
    xpath = pegar_xpath(n)
    #print("XPath do elemento:", xpath)
    print(n.text)

    materia_tipo = browser.find_element(By.XPATH, f'{xpath}')
    text = materia_tipo.text

    if text == '':
        break
    else:
        lista_cursos.append(text)

browser.implicitly_wait(5)
pesquisar_materia_btn = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/span[2]/a')
pesquisar_materia_btn.click()
for e in lista_cursos:
    browser.implicitly_wait(5)
    pesquisar_materia = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/span[1]/div/input')
    pesquisar_materia.send_keys(Keys.CONTROL + 'a')
    pesquisar_materia.send_keys(f'{e}')
    pesquisar_materia.send_keys(Keys.ENTER)

    # Sempre o mesmo xpath ao pesquisar a matéria e assunto
    time.sleep(5)
    browser.implicitly_wait(5)
    materia_tipo_geral_fixo = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/div/span[2]')
    materia_tipo_geral_fixo.click()
    time.sleep(3)

    #materia_tipo_geral_fixo = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/div/span[2]/span[2]')

    print('passou1')
    print('passou2')
    time.sleep(3)
    browser.implicitly_wait(2)
    sublista_element_1 = browser.find_element(By.XPATH, '//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li')
    sublista_element = sublista_element_1.find_elements(By.TAG_NAME, 'li')
    qtd_sublistas = len(sublista_element)
    print('qtd sublista',qtd_sublistas )
    print('passou3')
    #print('CHEGOU')
    for o in range(qtd_sublistas):
        print('range: ', o)
        #print('ENTROU')
        try:
            xpath_caminho = f'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[{o + 1}]/div/span[2]/span[2]'
            xpath_li_element = f'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[{o + 1}]'
            print('foi1')
            time.sleep(0.5)
            li_element = browser.find_element(By.XPATH, f'{xpath_li_element}')
            print('foi2')

            time.sleep(0.5)
            verif_subcat = li_element.find_element(By.TAG_NAME, 'ul')
            print('foi3')
            print('DEU')


            time.sleep(0.5)
            div_element = browser.find_element(By.XPATH, f'{xpath_caminho}')
            print(div_element.text)
            print('foi4')
            div_element.click()
            print('foi5')
        except:
            # Procorar elemento div
            time.sleep(0.5)
            div_element = browser.find_element(By.XPATH, f'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[{o+1}]/div/span[2]/span[2]')
            time.sleep(0.5)
            print(div_element.text)


            print('passou4')

    """
        #vvvvv verifica se há sublistas no assunto selecionado
        vf_assunto = 0
        for p in range(len(div_element)):
            browser.implicitly_wait(2)
            texto_assunto = ''

            try:
                span_element = browser.find_element(By.XPATH, f'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[1]/div/span[2]')
                texto_assunto = span_element.text                   #'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[2]/div/span[2]'
                if texto_assunto != '':                             #'//*[@id="caderno-novo"]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/ul/li/ul/li/ul/li[3]/div/span[2]'
                    print('Assunto: ', texto_assunto)
                    # Procurar Icone da sublista:

                else:
                    print('o campo e vazio')
            except:
                vf_assunto += vf_assunto
                print('span elemet não existe...')

                
                vf_assunto += vf_assunto
                if vf_assunto >= 1:
                    vf_assunto = 0
                    new_span_element = p.find_element(By.CLASS_NAME, 'arvore-item-icone-nome-wrap')
                    new_span_element.click()

                    new_sublista = new_span_element.find_elements(By.CLASS_NAME, 'arvore ng-scope ng-isolate-scope')

                    for a in new_sublista:
                        browser.implicitly_wait(2)
                        new_div_element = o.find_elements(By.TAG_NAME, 'div')
                        print('passou5')

                        for b in new_sublista:
                            browser.implicitly_wait(2)
                            span_element = b.find_element(By.CLASS_NAME, 'arvore-item-icone-nome-wrap')
                            texto_assunto = span_element.text
                            if texto_assunto != '':
                                print('Su assunto: ', texto_assunto)
                            else:
                                print('o campo e vazio')
            """





