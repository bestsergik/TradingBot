from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QPushButton, QLabel, QTabWidget, QTableWidget, QLineEdit, QComboBox, QPlainTextEdit,
                               QHBoxLayout)
from PySide6.QtCore import Qt


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Главный виджет и лэйаут
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Панель состояния
        self.status_bar = self.statusBar()
        self.connection_status = QLabel("Disconnected")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.pause_button = QPushButton("Pause")
        self.balance_label = QLabel("Balance: 0.0 BTC")
        self.status_bar.addPermanentWidget(self.start_button)
        self.status_bar.addPermanentWidget(self.stop_button)
        self.status_bar.addPermanentWidget(self.pause_button)
        self.status_bar.addWidget(self.connection_status)
        self.status_bar.addPermanentWidget(self.balance_label)

        # Вкладки
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # Вкладка Графика
        self.chart_tab = QWidget()
        self.tabs.addTab(self.chart_tab, "Chart")

        # Вкладка Текущих Позиций
        self.positions_tab_widget = QWidget()  # Создаем новый виджет
        self.positions_tab = QVBoxLayout(self.positions_tab_widget)  # Присваиваем QVBoxLayout этому виджету
        self.positions_table = QTableWidget(5, 3)
        self.positions_tab.addWidget(self.positions_table)
        self.tabs.addTab(self.positions_tab_widget, "Current Positions")

        # Вкладка Истории Торгов
        self.history_tab_widget = QWidget()  # Создаем новый виджет
        self.history_tab = QVBoxLayout(self.history_tab_widget)  # Присваиваем QVBoxLayout этому виджету
        self.history_table = QTableWidget(5, 3)
        self.history_tab.addWidget(self.history_table)
        self.tabs.addTab(self.history_tab_widget, "Trade History")

        # Вкладка Логов
        self.log_tab_widget = QWidget()  # Создаем новый виджет
        self.log_tab = QVBoxLayout(self.log_tab_widget)  # Присваиваем QVBoxLayout этому виджету
        self.log_text = QPlainTextEdit()
        self.log_tab.addWidget(self.log_text)
        self.tabs.addTab(self.log_tab_widget, "Logs")

        # Настройки стратегий
        self.strategy_tab_widget = QWidget()  # Создаем новый виджет
        self.strategy_tab = QVBoxLayout(self.strategy_tab_widget)  # Присваиваем QVBoxLayout этому виджету
        self.strategy_selector_label = QLabel("Select Strategy:")
        self.strategy_selector = QComboBox()
        self.strategy_parameter_input = QLineEdit("Parameter Input")
        strategy_layout = QHBoxLayout()
        strategy_layout.addWidget(self.strategy_selector_label)
        strategy_layout.addWidget(self.strategy_selector)
        strategy_layout.addWidget(self.strategy_parameter_input)
        self.strategy_tab.addLayout(strategy_layout)
        self.tabs.addTab(self.strategy_tab_widget, "Strategy Settings")

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Crypto Trading Bot')
        self.show()

    def initUI(self):
        # Set window size, title, and show it
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Crypto Trading Bot')

        # Basic styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #333;
            }
            QLabel, QPushButton, QPlainTextEdit, QTableWidget {
                font-family: "Arial";
                font-size: 14px;
            }
            QLabel {
                color: #FFF;
            }
            QPushButton {
                background-color: #555;
                color: #FFF;
                border: none;
                padding: 5px 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #666;
            }
            QTabWidget::pane {
                border: none;
            }
            QTabBar::tab {
                background: #555;
                color: #FFF;
                padding: 10px;
                border: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected {
                background: #666;
            }
        """)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    myapp = MyApp()
    app.exec()
