from PySide6 import QtWidgets  
import sys  

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Indication COM-port")
window.resize(1500, 500)

lbl = QtWidgets.QLabel("Графики")

# Создание кнопки с надписью "Close"
btn = QtWidgets.QPushButton("Close")


box = QtWidgets.QVBoxLayout()

# Добавление метки и кнопки в вертикальный блок
box.addWidget(lbl)
box.addWidget(btn)

# Установка вертикального блока в качестве компоновщика главного окна
window.setLayout(box)

# Подключение обработчика события "clicked" кнопки к методу app.quit, вызывающему завершение приложения
btn.clicked.connect(app.quit)

# Отображение главного окна
window.show()

# Запуск основного цикла обработки событий приложения
sys.exit(app.exec())  # После завершения цикла приложение выходит из программы
