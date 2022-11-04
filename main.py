from random import randint
from sys import argv

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class LixoNaCidade:
    def __init__(self):
        # postos de deposito de lixo
        self.postos = {"Mapunda": 0,
                       "Minhota": 0,
                       "Arco Iris": 0,
                       "Lucrecia": 0,
                       "Lage": 0,
                       "Tchioco": 0,
                       "Laureanos": 0,
                       "Bairro Comercial": 0}
        self.bairros = list(self.postos.keys())

        self.app = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Lixo na Cidade")
        # self.ferramentas.setFixedSize(400, 400)
        self.ferramentas.setStyleSheet(theme)

        self.mainpage()

    def mainpage(self):

        def recolher(_local: str = None):
            if _local:
                pass
            else:
                label1.setText(f"Posto\n{self.bairros[0]}\n\n{self.postos[self.bairros[0]]}kg")
                label2.setText(f"Posto\n{self.bairros[1]}\n\n{self.postos[self.bairros[1]]}kg")
                label3.setText(f"Posto\n{self.bairros[2]}\n\n{self.postos[self.bairros[2]]}kg")
                label4.setText(f"Posto\n{self.bairros[3]}\n\n{self.postos[self.bairros[3]]}kg")
                label5.setText(f"Posto\n{self.bairros[4]}\n\n{self.postos[self.bairros[4]]}kg")
                label6.setText(f"Posto\n{self.bairros[5]}\n\n{self.postos[self.bairros[5]]}kg")
                label7.setText(f"Posto\n{self.bairros[6]}\n\n{self.postos[self.bairros[6]]}kg")
                label8.setText(f"Posto\n{self.bairros[7]}\n\n{self.postos[self.bairros[7]]}kg")
            layout.update()

        def carregarpostos():
            label1.setText(f"Posto\n{self.bairros[0]}\n\n{self.postos[self.bairros[0]]+randint(1, 100)}kg")
            label2.setText(f"Posto\n{self.bairros[1]}\n\n{self.postos[self.bairros[1]]+randint(1, 100)}kg")
            label3.setText(f"Posto\n{self.bairros[2]}\n\n{self.postos[self.bairros[2]]+randint(1, 100)}kg")
            label4.setText(f"Posto\n{self.bairros[3]}\n\n{self.postos[self.bairros[3]]+randint(1, 100)}kg")
            label5.setText(f"Posto\n{self.bairros[4]}\n\n{self.postos[self.bairros[4]]+randint(1, 100)}kg")
            label6.setText(f"Posto\n{self.bairros[5]}\n\n{self.postos[self.bairros[5]]+randint(1, 100)}kg")
            label7.setText(f"Posto\n{self.bairros[6]}\n\n{self.postos[self.bairros[6]]+randint(1, 100)}kg")
            label8.setText(f"Posto\n{self.bairros[7]}\n\n{self.postos[self.bairros[7]]+randint(1, 100)}kg")
            layout.update()
            postocheio()

        def postocheio():
            if self.postos[self.bairros[0]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[1]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[2]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[3]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[4]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[5]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[6]] > 50:
                label1.setStyleSheet("background-color: red;")
            elif self.postos[self.bairros[7]] > 50:
                label1.setStyleSheet("background-color: red;")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        posto1 = QFrame()
        layout1 = QVBoxLayout()
        label1 = QLabel(f"Posto\n{self.bairros[0]}\n\n{self.postos[self.bairros[0]]}kg")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local1 = QPushButton("Recolha Localizada")
        layout1.addWidget(label1)
        layout1.addWidget(recolha_local1)
        posto1.setLayout(layout1)

        posto2 = QFrame()
        layout2 = QVBoxLayout()
        label2 = QLabel(f"Posto\n{self.bairros[1]}\n\n{self.postos[self.bairros[1]]}kg")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local2 = QPushButton("Recolha Localizada")
        layout2.addWidget(label2)
        layout2.addWidget(recolha_local2)
        posto2.setLayout(layout2)

        posto3 = QFrame()
        layout3 = QVBoxLayout()
        label3 = QLabel(f"Posto\n{self.bairros[2]}\n\n{self.postos[self.bairros[2]]}kg")
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local3 = QPushButton("Recolha Localizada")
        layout3.addWidget(label3)
        layout3.addWidget(recolha_local3)
        posto3.setLayout(layout3)

        posto4 = QFrame()
        layout4 = QVBoxLayout()
        label4 = QLabel(f"Posto\n{self.bairros[3]}\n\n{self.postos[self.bairros[3]]}kg")
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local4 = QPushButton("Recolha Localizada")
        layout4.addWidget(label4)
        layout4.addWidget(recolha_local4)
        posto4.setLayout(layout4)

        posto5 = QFrame()
        layout5 = QVBoxLayout()
        label5 = QLabel(f"Posto\n{self.bairros[4]}\n\n{self.postos[self.bairros[4]]}kg")
        label5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local5 = QPushButton("Recolha Localizada")
        layout5.addWidget(label5)
        layout5.addWidget(recolha_local5)
        posto5.setLayout(layout5)

        posto6 = QFrame()
        layout6 = QVBoxLayout()
        label6 = QLabel(f"Posto\n{self.bairros[5]}\n\n{self.postos[self.bairros[5]]}kg")
        label6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local6 = QPushButton("Recolha Localizada")
        layout6.addWidget(label6)
        layout6.addWidget(recolha_local6)
        posto6.setLayout(layout6)

        posto7 = QFrame()
        layout7 = QVBoxLayout()
        label7 = QLabel(f"Posto\n{self.bairros[6]}\n\n{self.postos[self.bairros[6]]}kg")
        label7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local7 = QPushButton("Recolha Localizada")
        layout7.addWidget(label7)
        layout7.addWidget(recolha_local7)
        posto7.setLayout(layout7)

        posto8 = QFrame()
        layout8 = QVBoxLayout()
        label8 = QLabel(f"Posto\n{self.bairros[7]}\n\n{self.postos[self.bairros[7]]}kg")
        label8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        recolha_local8 = QPushButton("Recolha Localizada")
        layout8.addWidget(label8)
        layout8.addWidget(recolha_local8)
        posto8.setLayout(layout8)

        layout_labels = QGridLayout()
        layout_labels.addWidget(posto1, 1, 1)
        layout_labels.addWidget(posto2, 1, 2)
        layout_labels.addWidget(posto3, 1, 3)
        layout_labels.addWidget(posto4, 1, 4)
        layout_labels.addWidget(posto5, 2, 1)
        layout_labels.addWidget(posto6, 2, 2)
        layout_labels.addWidget(posto7, 2, 3)
        layout_labels.addWidget(posto8, 2, 4)
        layout.addLayout(layout_labels)

        layout_btns = QHBoxLayout()
        carregar_postos = QPushButton("Carregar Postos")
        carregar_postos.pressed.connect(carregarpostos)
        layout_btns.addWidget(carregar_postos)
        recolha_geral = QPushButton("Recolha Geral")
        recolha_geral.pressed.connect(recolher)
        layout_btns.addWidget(recolha_geral)
        layout.addLayout(layout_btns)

        self.ferramentas.setLayout(layout)



if __name__ == '__main__':
    theme = open("./theme/lixonacidade.qss").read().strip()
    ngc = LixoNaCidade()
    ngc.ferramentas.show()
    ngc.app.exec()
