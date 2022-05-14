#import PySimpleGUI as sg
import pyautogui as pg
import sys

SUBJECTS = [
    'Outra',
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
    'Inglês'
]

class Gui_pg:
    def __init__(self):
        self.subjects = SUBJECTS
        self.program_name = 'Automação gdocs'
              
    def usuario_permitir_iniciar(self):
        resposta_do_usuario = pg.confirm('Iniciar script de automação?', self.program_name, ['Ok', 'Cancelar'])                                 
        if resposta_do_usuario == 'Ok':
            return True
        return False
    
    def escolher_materia(self):
        materia = pg.confirm('Escolha a matéria do documento', self.program_name, self.subjects)
        if materia == 'Outra':
            materia = pg.prompt('Digite a matéria específica: ', self.program_name) 
        if materia is None:
            return False
        return materia
    
    def mostrar_fim_do_programa(self):
        text = 'Script de automação finalizado'
        return pg.alert(text, self.program_name, 'OK')
        