import sys
from PyQt6 import QtWidgets
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QTableView, QPushButton
import os


class CoffeeApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Database")
        self.setGeometry(100, 100, 800, 600)
        self.db = None
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)
        self.load_button = QPushButton("Загрузить данные", self)
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)
        self.setLayout(layout)

    def init_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        if not db.open():
            raise Exception("Не удалось открыть базу данных.")
        return db

    def load_data(self):
        if not self.db:
            self.db = self.init_db()

        model = QSqlTableModel(self, self.db)
        model.setTable("coffee")
        model.select()
        self.table_view.setModel(model)
        self.table_view.setColumnHidden(0, True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
