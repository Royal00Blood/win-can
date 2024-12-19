import sys
from PySide6 .QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Win_form(QDialog):

    def __init__(self, parent = None):
        super(Win_form, self).__init__(parent)
        self.setWindowTitle("Soft COM-port")
        self.edit = QLineEdit("Напишите что-то...")
        self.button = QPushButton("Показать приветствие")
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.greetings)
    
    def greetings(self):
        print( f"Hi. {self.edit.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_form = Win_form()
    win_form.show()
    sys.exit(app.exec())


