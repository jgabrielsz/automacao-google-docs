from metodos_especificos import *
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
    
    def titulo(self):
        sleep(3)
        escrever(f'Atividade de {self.materia}')
        sleep(3)
        selecionar_acima()
        sleep(3)
        tornar_titulo()
        sleep(3)
        alinhar_texto_centro()
        sleep(3)
        negrito()
        sleep(3)
        #tamanho_fonte(20)
        #sleep(3)
        press('end')
        sleep(3)
        press('enter')
    
    def escrever_data(self):
        pass
    
    def escrever_meu_nome_e_nome_professor(self):
        pass
