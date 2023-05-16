import pyautogui
from time import sleep

usuario = 'usuario'
senha = 'senha'

pyautogui.alert('Ligando o robô. Favor não usar mouse ou teclado')

#Abrindo chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')
sleep(5)

#aceso freto
pyautogui.write('https://www.freto.com.br/Login')
pyautogui.press('enter')
sleep(5)

pyautogui.press('tab')
pyautogui.write(usuario)

pyautogui.press('tab')
pyautogui.write(senha)

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

#bloco de notas
pyautogui.press('winleft')
pyautogui.write('bloco de notas')
pyautogui.press('enter')
sleep(5)
pyautogui.hotkey('winleft', 'right')

pyautogui.alert('Fim')

