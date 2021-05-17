import pyautogui as pg
import sys
from interação_GUI import Gui_pg
from manipular_docs import ManipularDocs

class Automação:
    def __init__(self):
        self.interação_gui = Gui_pg()
    
    def iniciar(self):
        self.permitir_execução_por_gui()
        materia = self.escolher_materia_por_GUI()
        self.escrever_no_documento(materia)
        self.informar_que_o_programa_foi_finalizado()
        
    def permitir_execução_por_gui(self):
        if self.interação_gui.usuario_permitir_iniciar():
            return
        sys.exit()

    def escolher_materia_por_GUI(self):
        materia =  self.interação_gui.escolher_materia()
        if materia is None or materia: # Passar somente se materia =! None
            return materia
        sys.exit()

    def escrever_no_documento(self, materia):
        docs = ManipularDocs(materia)
        docs.escrever_titulo()
        docs.escrever_data()
        docs.escrever_meu_nome_e_nome_professor()
        docs.definir_titulo()

    def informar_que_o_programa_foi_finalizado(self):
        self.interação_gui.mostrar_fim_do_programa()

        


executar = Automação()
executar.iniciar()
