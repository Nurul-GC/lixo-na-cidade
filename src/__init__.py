from os.path import curdir, abspath
from sys import argv, exit
from schedule import *

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication, QMenuBar, QMessageBox, QWidget, QVBoxLayout


class LixoNaCidade:
    def __init__(self):
        layout = QVBoxLayout()
        self.ferramenta = QWidget()
        self.ferramenta.setStyleSheet(theme)
        self.ferramenta.setWindowIcon(QIcon(f"{abspath(curdir)}/favicon/favicon-512x512.png"))
        self.ferramenta.setWindowTitle("Lixo em Angola")

        self.webpage = QWebView()
        self.webpage.load(QUrl.fromLocalFile(f"{abspath(curdir)}/html/index.html"))
        layout.addWidget(self.webpage)

        menu = QMenuBar(self.ferramenta)
        detalhes = menu.addMenu("Detalhes")
        instr = detalhes.addAction("Apresentação")
        instr.triggered.connect(self.instr)
        detalhes.addSeparator()
        sair = detalhes.addAction("Sair")
        sair.triggered.connect(self.sair)
        sobre = menu.addAction("Sobre")
        sobre.triggered.connect(self.sobre)
        layout.setMenuBar(menu)
        self.ferramenta.setLayout(layout)

    def atualizarpage(self):
        return self.webpage.reload()

    def sair(self):
        perg = QMessageBox.question(self.ferramenta, "Terminar o Programa",
                                    "Tem a certeza que deseja terminar o programa?")
        if perg.Yes:
            exit(0)

    def sobre(self):
        QMessageBox.information(self.ferramenta, "Sobre", """
<h2>Informações sobre o Programa</h2><hr>
<p>
<ul><li>Nome: Lixo em Angola</li>
<li>Versão: 0.1-072022demo</li>
<li>Programador & Designer: &copy; 2022 Nurul-GC<li></ul>
</p>
""")

    def instr(self):
        QMessageBox.information(self.ferramenta, "Apresentação", """
<img src="favicon/favicon-192x192.png" alt="logo" height="64" width="64">
<h2>Apresentação do Projecto</h2><hr>

<p>
<b>Problema de Investigação</b>
<ul><li>Lixo em Angola;</li></ul>
</p>

<p>
<b>Descrição</b>
<ul><li>Os amontoados de lixo nos centros urbanos e rurais como consequência de situações 
potencialmente milindrosas para a saúde e desenvolvimento social da comunidade;</li></ul>
</p> 

<p>
<b>Objecto de Estudo</b>
<ul><li>O problema em si (O lixo);</li></ul>
</p>

<p>
<b>Campo de Estudo</b>
<ul><li>Os centros urbanos e rurais;</li></ul>
</p>

<p>
<b>Perguntas de Investigação</b>
<ul><li>Como terminar com os amontoados de lixo nos centros urbanos e rurais?</li>
<li>Porquê o fluxo de lixo nos centros urbanos e rurais continuam aumentando?</li>
<li>Como a população está concencializada sobre a situação?</li>
<li>Qual o papel do cidadão na preservação do meio ambiente?</li>
<li>Como usar a tecnologia para resolver este problema?</li></ul>
</p>

<p>
<b>Objectivos</b>
<ul><li>Achar uma solução eficaz para o problema;</li>
<li>Usar meios tecnológicos para resolução 
do problema;</li>
<li>Concencializar a comunidade sobre a praticabilidade e eficácia das tecnologias na resolução de 
problemas quotidianos (semelhantes);</li></ul>
</p>
""")


if __name__ == '__main__':
    theme = open("theme/lixonacidade.qss").read().strip()
    app = QApplication(argv)
    gc = LixoNaCidade()
    every(5).seconds.do(gc.atualizarpage)
    gc.ferramenta.show()
    app.exec()
    while True:
        run_pending()
