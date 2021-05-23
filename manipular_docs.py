import metodos_especificos as mt
import pyautogui as pg
from time import sleep


MATERIAS_PROFESSORES = {
            'História': 'Felipe Fladson',
            'Biologia': 'Bisneto Maia',
            'Português': 'Gegardenia Santos',
            'Restabelecimento de uma Estação de Trabalho': 'Otávio Leopoldino Machado',
            'Otimização de uma Estação de Trabalho': 'Otávio Leopoldino Machado',
            'Assistência Informática': 'Otávio Leopoldino Machado',
            'Espanhol': 'Paulo Ricardo Monteiro',
            'Inglês': 'Priscila Lima',
            'Matemática': 'Rafael Silva Castro',
            'Química': 'Silvério Ferreira',
            'Geografia': 'Yris',
            'Educação Física': 'Umelber Henrique',
            'Física': 'Vanderlânia Felicio',
            'Filosofia': 'Otacílio',
            'Sociologia': 'Otacílio'
        }

PROFESSORES_M = [
            'Otávio Leopoldino Machado',
            'Bisneto Maia',
            'Paulo Ricardo Monteiro',
            'Rafael Silva Castro',
            'Silvério Ferreira',
            'Umelber Henrique',
            'Otacílio'
        ]

class ManipularDocs:
    
    def __init__(self, materia):
        self.materia = materia
    
    def escrever_titulo(self):
        mt.escrever(f'Atividade de {self.materia}')
        mt.selecionar_acima()
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
