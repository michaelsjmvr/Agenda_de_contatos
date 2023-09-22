import sys
import sqlite3
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox

# Definindo a classe principal do aplicativo
class AgendaDeContatos(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações iniciais da janela principal
        self.setWindowTitle("Agenda de Contatos")  # Define o título da janela
        self.setGeometry(100, 100, 400, 400)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QVBoxLayout(central_widget)  # Cria um layout de grade vertical para organizar os elementos

        # Elementos da interface gráfica
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome")  # Placeholder para o campo de nome
        self.telefone_input = QLineEdit(self)
        self.telefone_input.setPlaceholderText("Telefone")  # Placeholder para o campo de telefone
        self.adicionar_button = QPushButton("Adicionar", self)
        self.adicionar_button.clicked.connect(self.adicionar_contato)  # Conecta o botão ao método adicionar_contato

        # Área de pesquisa
        self.pesquisa_input = QLineEdit(self)
        self.pesquisa_input.setPlaceholderText("Pesquisar Contato")  # Placeholder para a área de pesquisa
        self.pesquisa_input.textChanged.connect(self.filtrar_contatos)  # Conecta a área de pesquisa ao método filtrar_contatos

        self.contatos_list = QListWidget(self)  # Lista de contatos

        # Botão para deletar contato
        self.deletar_button = QPushButton("Deletar", self)
        self.deletar_button.clicked.connect(self.deletar_contato)  # Conecta o botão ao método deletar_contato

        # Adiciona os elementos ao layout vertical
        layout.addWidget(self.nome_input)
        layout.addWidget(self.telefone_input)
        layout.addWidget(self.adicionar_button)
        layout.addWidget(self.pesquisa_input)  # Adicione a área de pesquisa
        layout.addWidget(self.contatos_list)
        layout.addWidget(self.deletar_button)  # Adicione o botão "Deletar"

        # Cria uma conexão com o banco de dados SQLite3
        self.conexao = sqlite3.connect("agenda.db")
        self.criar_tabela_contatos()  # Chama o método para criar a tabela de contatos no banco de dados

        self.carregar_contatos()  # Chama o método para carregar os contatos existentes

    # Método para criar a tabela de contatos no banco de dados
    def criar_tabela_contatos(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                telefone TEXT
            )
        ''')
        self.conexao.commit()

    # Método para adicionar um contato
    def adicionar_contato(self):
        nome = self.nome_input.text()
        telefone = self.telefone_input.text()
        if nome and telefone:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", (nome, telefone))
            self.conexao.commit()

            contato = f"Nome: {nome}, Telefone: {telefone}"
            self.contatos_list.addItem(contato)
            self.nome_input.clear()
            self.telefone_input.clear()
        else:
            self.mostrar_mensagem("Erro", "Preencha todos os campos.")

    # Método para exibir uma mensagem de erro em uma caixa de diálogo
    def mostrar_mensagem(self, titulo, mensagem):
        mensagem_box = QMessageBox(self)
        mensagem_box.setWindowTitle(titulo)
        mensagem_box.setText(mensagem)
        mensagem_box.setStandardButtons(QMessageBox.Ok)
        mensagem_box.exec()

    # Método para filtrar contatos com base na pesquisa
    def filtrar_contatos(self):
        filtro = self.pesquisa_input.text().strip().lower()
        self.contatos_list.clear()
        cursor = self.conexao.cursor()
        cursor.execute("SELECT nome, telefone FROM contatos WHERE LOWER(nome) LIKE ?", ('%' + filtro + '%',))
        for row in cursor.fetchall():
            contato = f"Nome: {row[0]}, Telefone: {row[1]}"
            self.contatos_list.addItem(contato)

    # Método para deletar um contato
    def deletar_contato(self):
        item_selecionado = self.contatos_list.currentItem()
        if item_selecionado:
            item_text = item_selecionado.text()
            nome = item_text.split(",")[0].split(":")[1].strip()
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM contatos WHERE nome=?", (nome,))
            self.conexao.commit()
            self.contatos_list.takeItem(self.contatos_list.row(item_selecionado))

    # Método para carregar contatos existentes no banco de dados
    def carregar_contatos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT nome, telefone FROM contatos")
        for row in cursor.fetchall():
            contato = f"Nome: {row[0]}, Telefone: {row[1]}"
            self.contatos_list.addItem(contato)

# Função principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    agenda = AgendaDeContatos()
    agenda.show()
    sys.exit(app.exec())
