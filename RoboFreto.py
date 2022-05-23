import pyautogui
from time import sleep

pyautogui.alert('Ligando o robô. Favor não usar mouse ou teclado')

#Abrindo chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')
sleep(5)

#aceso freto
pyautogui.write('file:///C:/Users/lukin/OneDrive/%C3%81rea%20de%20Trabalho/Estudos/GitHub%20projetos/Freto-BKO-main/index.html')
pyautogui.press('enter')
sleep(5)

pyautogui.press('tab')
pyautogui.write('lucas')

pyautogui.press('tab')
pyautogui.write('123')

pyautogui.press('tab')
pyautogui.press('enter')

#acesso consulta
pyautogui.hotkey('ctrl', 't')
sleep(5)
pyautogui.write('consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/consultapublica')
pyautogui.press('enter')

#acesso whatsapp
pyautogui.hotkey('ctrl', 't')
sleep(5)
pyautogui.write('web.whatsapp.com')
pyautogui.press('enter')

pyautogui.alert('Fim')

