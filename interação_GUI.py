#import PySimpleGUI as sg
import pyautogui as pg
import sys

MATERIAS = [
    'Português',
    'Química',
    'Filosofia',
    'Matemática',
    'Física',
    'Geografia',
    'Biologia',
    'Assistência Informática',
    'Espanhol',
    'Educação Física',
    'Restabelecimento de uma Estação de Trabalho',
    'Otimização de uma Estação de Trabalho',
    'História',
    'Sociologia',
    'Inglês',
    'Outra'
]

class Gui_pg:
    def __init__(self):
        self.materias = MATERIAS
        self.nome_programa = 'Automação gdocs'
              
    def usuario_permitir_iniciar(self):
        resposta_do_usuario = pg.confirm('Iniciar script de automação?', self.nome_programa, ['Ok', 'Cancelar'])                                 
        if resposta_do_usuario == 'Ok':
            return True
        return False
    
    def escolher_materia(self):
        materia = pg.confirm('Escolha a matéria do documento', self.nome_programa, self.materias)
        if materia == 'Outra':
            materia = pg.prompt('Digite a matéria específica: ', self.nome_programa) 
        if materia is None:
            return False
        return materia
    
    def mostrar_fim_do_programa(self):
        text = 'Script de automação finalizado\nO link do docs está na sua área de transferência.'
        return pg.alert(text, self.nome_programa, 'OK')



#pg.password(text='sua senha', title='password', default='senha', mask='*')