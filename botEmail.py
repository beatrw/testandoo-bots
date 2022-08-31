#Testando bot web
#Bot que entra no email

from lib2to3.pgen2 import driver
from selenium import webdriver
#Para gerenciar o webdriver, atualizações automáticas etc
from webdriver_manager.chrome import ChromeDriverManager
#Para buscar os elementos da página
from selenium.webdriver.common.by import By
import time


"""
Pra resolver o erro do log(?):
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
"""


#Abrindo o navegador
class botmail():
    def mmail(self):
        navegador = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #Entrando no site
        navegador.get("https://login.live.com/")
        navegador.maximize_window() 
        print(navegador.title) #Pra dizer os sites que ta entrando/o que ta fazendo
        #Usando find_element pra encontrar a posição do site pra clicar etc:
        #Usando send_keys pra escrever na posição:
        navegador.find_element(By.CSS_SELECTOR, "#i0116").send_keys(EMAIL)
        #Tempo entre as operações
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, "#idSIButton9").click()

        navegador.find_element(By.CSS_SELECTOR,"#i0118").send_keys(SENHA)
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, "#idBtn_Back").click()
        input()

entMai = botmail()
entMai.mmail()

