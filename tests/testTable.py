import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout)

class TableWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("PyQt6 QTableWidget Example")
        self.setGeometry(100, 100, 500, 300)
        self.setStyleSheet("background-color: white;") # Set background color
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(["Color Name", "Hex Code"]) # Set headers
        self.tableWidget.setStyleSheet("background-color: white; color: black;") # Set background color
        

        self.load_data(data)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def load_data(self, data):
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(item))) # Add item to cell

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Sample data: list of tuples (name, hex code)
    colors = [("Red", "#FF0000"), ("Green", "#00FF00"), ("Blue", "#0000FF"),
            ("Black", "#000000"), ("White", "#FFFFFF")]
    window = TableWindow(colors)
    window.show()
    sys.exit(app.exec())
