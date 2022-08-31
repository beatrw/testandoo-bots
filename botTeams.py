#Testando bot desktop
#Bot que abre o teams e envia mensagem(?)

import time
import pyautogui


#Setando intervalo entre comandos(em seg)
pyautogui.PAUSE = 1.5

#Abrindo o programa
pyautogui.press("win")
pyautogui.write("teams")
pyautogui.press("enter")

#Encontrando a posição do mouse pra setar os cliques
"""
time.sleep(3)
print(pyautogui.position())
"""

#Mexendo dentro do programa
pyautogui.click(x=547, y=46)
pyautogui.write(NOME_PESSOA)
pyautogui.click(x=453, y=165)
pyautogui.write("Oi")
pyautogui.press("enter")


