from pyautogui import *
from pyperclip import copy
from datetime import datetime


# Funções Gerais
data_de_hoje = lambda: datetime.now().strftime('%d/%m/%Y')
def escrever(text):
    copy(text)
    hotkey('ctrl', 'v') 


# Manipulação do docs
negrito = lambda: hotkey('ctrl', 'b')
tornar_texto_normal = lambda: hotkey('ctrl', 'alt', '0')
tornar_titulo = lambda: hotkey('ctrl', 'alt', '1')
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
    escrever('renomear')
    press('enter')
    press('enter')

