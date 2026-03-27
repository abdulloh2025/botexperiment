import sys
import pyodbc
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)


try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=WIN-O895RANEHB5\\SQLEXPRESS;"
        "DATABASE=Minimarket;"
        "Trusted_Connection=yes;"
    )
except Exception as e:
    print("SQL Connection Error:", e)
    sys.exit()

# ================== BUTTON STYLE ==================
def style_buttons(btn_insert, btn_select, btn_update, btn_delete):
    btn_insert.setStyleSheet("""
        QPushButton { background-color:#28a745; color:white; font-weight:bold; border-radius:6px; padding:5px 10px; }
        QPushButton:hover { background-color:#218838; }
    """)
    btn_select.setStyleSheet("""
        QPushButton { background-color:#007bff; color:white; font-weight:bold; border-radius:6px; padding:5px 10px; }
        QPushButton:hover { background-color:#0069d9; }
    """)
    btn_update.setStyleSheet("""
        QPushButton { background-color:#ffc107; color:black; font-weight:bold; border-radius:6px; padding:5px 10px; }
        QPushButton:hover { background-color:#e0a800; }
    """)
    btn_delete.setStyleSheet("""
        QPushButton { background-color:#dc3545; color:white; font-weight:bold; border-radius:6px; padding:5px 10px; }
        QPushButton:hover { background-color:#c82333; }
    """)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQL CRUD")
        self.resize(800, 600)

        self.title = QLabel("Jadvalni tanlang:")

        self.table_select = QComboBox()
        self.refresh_table_list()

        self.table_select.currentTextChanged.connect(self.load_columns)

        self.inputs_layout = QVBoxLayout()

        self.btn_insert = QPushButton("INSERT")
        self.btn_select = QPushButton("SELECT")
        self.btn_update = QPushButton("UPDATE")
        self.btn_delete = QPushButton("DELETE")

        style_buttons(self.btn_insert, self.btn_select, self.btn_update, self.btn_delete)

        self.btn_insert.clicked.connect(self.insert_data)
        self.btn_select.clicked.connect(self.select_data)
        self.btn_update.clicked.connect(self.update_data)
        self.btn_delete.clicked.connect(self.delete_data)

        btns = QHBoxLayout()
        btns.addWidget(self.btn_insert)
        btns.addWidget(self.btn_select)
        btns.addWidget(self.btn_update)
        btns.addWidget(self.btn_delete)

        self.table = QTableWidget()
        self.table.cellClicked.connect(self.fill_inputs)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.table_select)
        layout.addLayout(self.inputs_layout)
        layout.addLayout(btns)
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_columns(self.table_select.currentText())


    def show_error(self, msg):
        QMessageBox.critical(self, "Xatolik", msg)

    def clear_inputs(self):
        for field in self.inputs.values():
            field.clear()
        self.table.clearSelection()

    def refresh_table_list(self):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_TYPE='BASE TABLE'
                  AND TABLE_SCHEMA='dbo'
                  AND TABLE_NAME NOT IN ('sysdiagrams')
            """)
            tables = [row[0] for row in cursor.fetchall()]
            self.table_select.clear()
            self.table_select.addItems(tables)
        except Exception as e:
            self.show_error(f"Jadval ro‘yxatini olishda xatolik:\n{e}")


    def load_columns(self, table_name):
        self.TABLE_NAME = table_name
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM [{table_name}] WHERE 1=0")
            self.columns = [desc[0] for desc in cursor.description]

            for i in reversed(range(self.inputs_layout.count())):
                widget = self.inputs_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            self.inputs = {}
            for col in self.columns[1:]:
                le = QLineEdit()
                le.setPlaceholderText(col)
                self.inputs_layout.addWidget(le)
                self.inputs[col] = le

            self.load_data()
        except Exception as e:
            self.show_error(f"Ustunlarni yuklashda xatolik:\n{e}")

    def load_data(self):
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM [{self.TABLE_NAME}]")
            rows = cursor.fetchall()

            self.table.setColumnCount(len(self.columns))
            self.table.setHorizontalHeaderLabels(self.columns)
            self.table.setRowCount(len(rows))

            for i, rowdata in enumerate(rows):
                for j, val in enumerate(rowdata):
                    self.table.setItem(i, j, QTableWidgetItem("" if val is None else str(val)))
        except Exception as e:
            self.show_error(f"Jadvalni yuklashda xatolik:\n{e}")

    def select_data(self):
        row = self.table.currentRow()
        if row < 0:
            return
        try:
            rasta_id_item = self.table.item(row, 0)
            if rasta_id_item is None:
                return
            rasta_id = rasta_id_item.text()

            cursor = conn.cursor()
            cursor.execute(
                "SELECT tur_nomi FROM MahsulotTuri WHERE rasta_id = ?",
                (rasta_id,)
            )
            rows = cursor.fetchall()

            self.table.clear()
            self.table.setRowCount(len(rows))
            self.table.setColumnCount(1)
            self.table.setHorizontalHeaderLabels(["Tur nomi"])

            for i, (tur,) in enumerate(rows):
                self.table.setItem(i, 0, QTableWidgetItem(str(tur)))
        except Exception as e:
            self.show_error(f"SELECT xatolik:\n{e}")

    def insert_data(self):
        try:
            cols = ", ".join(f"[{col}]" for col in self.inputs.keys())
            placeholders = ", ".join("?" for _ in self.inputs)
            values = []

            for col in self.inputs:
                val = self.inputs[col].text().strip()
                if val == "":
                    val = None
                elif col.lower() == "rasta_id":  # rasta_id faqat raqam bo‘lishi kerak
                    try:
                        val = int(val)
                    except ValueError:
                        self.show_error("Rasta_id faqat raqam bo‘lishi kerak")
                        return
                values.append(val)

            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO [{self.TABLE_NAME}] ({cols}) VALUES ({placeholders})",
                values
            )
            conn.commit()
            self.load_data()
            self.clear_inputs()
        except Exception as e:
            self.show_error(f"INSERT xatolik:\n{e}")

    def update_data(self):
        row = self.table.currentRow()
        if row < 0:
            return
        try:
            id_item = self.table.item(row, 0)
            if id_item is None:
                return
            id_ = id_item.text()

            set_clause = ", ".join(f"[{col}]=?" for col in self.inputs)
            values = []
            for col in self.inputs:
                val = self.inputs[col].text().strip()
                if val == "":
                    val = None
                values.append(val)
            values.append(id_)

            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE [{self.TABLE_NAME}] SET {set_clause} WHERE [{self.columns[0]}]=?",
                values
            )
            conn.commit()
            self.load_data()
            self.clear_inputs()
        except Exception as e:
            self.show_error(f"UPDATE xatolik:\n{e}")

    def delete_data(self):
        row = self.table.currentRow()
        if row < 0:
            return
        try:
            id_item = self.table.item(row, 0)
            if id_item is None:
                return
            id_ = id_item.text()

            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM [{self.TABLE_NAME}] WHERE [{self.columns[0]}]=?",
                (id_,)
            )
            conn.commit()
            self.load_data()
            self.clear_inputs()
        except Exception as e:
            self.show_error(f"DELETE xatolik:\n{e}")

    def fill_inputs(self, row, col):
        for idx, key in enumerate(self.inputs.keys(), start=1):
            item = self.table.item(row, idx)
            self.inputs[key].setText("" if item is None else item.text())


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
