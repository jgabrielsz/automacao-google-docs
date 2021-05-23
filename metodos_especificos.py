from pyautogui import hotkey, write, press
from pyperclip import copy
from datetime import datetime
import pyautogui

pyautogui.PAUSE = 1

# Funções Gerais
data_de_hoje = lambda: datetime.now().strftime('%d/%m/%Y')
def escrever(text):
    copy(text)
    hotkey('ctrl', 'v') 


# Manipulação do docs
negrito = lambda: hotkey('ctrl', 'b')
tornar_texto_normal = lambda: hotkey('ctrl', 'alt', '0')
tornar_titulo = lambda x: hotkey('ctrl', 'alt', f'{x}')
alinhar_texto_esquerda = lambda: hotkey('ctrl', 'shift', 'l')
alinhar_texto_direita = lambda: hotkey('ctrl', 'shift', 'r')
alinhar_texto_centro = lambda: hotkey('ctrl', 'shift', 'e')
menu_arquivo = lambda: hotkey('alt', 'shift', 'f')
selecionar_acima = lambda: hotkey('ctrl', 'shift', 'home')

def tamanho_fonte(tamanho):
    hotkey('alt', '/')
    write(f'Tamanho da fonte: {tamanho}')
    press('enter')

def renomear():
    hotkey('alt', '/')
    escrever('Renomear')
    press('enter')
    press('enter')

