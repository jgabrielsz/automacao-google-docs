import metodos_especificos as mt
import pyautogui as pg
from time import sleep


MATERIAS_PROFESSORES = {
            'Materia': 'Professor'
        }

PROFESSORES_M = [
            'Nome do professor'
        ]

class ManipularDocs:
    
    def __init__(self, materia):
        self.materia = materia
    
    def escrever_titulo(self):
        mt.escrever(f'Atividade de {self.materia}')
        mt.selecionar_tudo()
        mt.tornar_titulo(1)
        mt.alinhar_texto_centro()
        mt.negrito()
        mt.hotkey('ctrl', 'end')
        pg.press('enter')
    
    def escrever_data(self):
        mt.escrever(f'Data: {mt.data_de_hoje()}')
        pg.press('enter')
    
    def escrever_meu_nome_e_nome_professor(self):
        mt.escrever('Aluno: José Gabriel de Souza Silva')
        sleep(0.5)
        pg.press('enter')
        if self.materia in MATERIAS_PROFESSORES:
            if MATERIAS_PROFESSORES[self.materia] in PROFESSORES_M:
                mt.escrever(f'Professor: {MATERIAS_PROFESSORES[self.materia]}')
            else:
                mt.escrever(f'Professora: {MATERIAS_PROFESSORES[self.materia]}')
        else:
            mt.escrever('Professor')

    def definir_titulo(self):
        mt.renomear()
