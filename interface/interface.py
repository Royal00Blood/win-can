import sys
import serial
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class RealTimePlot(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Real-Time Data from COM Port")
        
        # Настройка COM порта
        self.serial_port = serial.Serial('COM3', 9600)  # Укажите Ваш COM порт
        self.data = []

        # Настройка интерфейса
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.indicator = QLabel("Indicator")
        self.layout.addWidget(self.indicator)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Real-Time Data Plot")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")

        # Таймер для обновления графика
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Обновление каждую секунду

    def update_plot(self):
        if self.serial_port.in_waiting > 0:
            line = self.serial_port.readline().decode('utf-8').strip()
            value = float(line)
            self.data.append(value)

            # Обновление цветового индикатора
            if value > 50:
                self.indicator.setStyleSheet("background-color: green;")
            else:
                self.indicator.setStyleSheet("background-color: red;")

            # Обновление графика
            self.ax.clear()
            self.ax.plot(self.data)
            self.ax.set_title("Real-Time Data Plot")
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Value")
            self.canvas.draw()

# if __name__ == "main":
app = QApplication(sys.argv)
window = RealTimePlot()
window.show()
sys.exit(app.exec())

