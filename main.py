import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCheckBox, QFrame, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
import sqlite3
import os


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("InlogPagina")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #4CAF50;")

        self.bovenform = QLabel("Chem2Go", self)
        self.bovenform.setFixedSize(300, 120)
        self.bovenform.setVisible(True)
        self.bovenform.move(200, 40)
        self.bovenform.setStyleSheet("background-color: #137827; " \
        "border: 2px solid black; font-size: 50px; font-weight: bold; color: white;")
        self.bovenform.setAlignment(Qt.AlignCenter)

        self.LogoBea = QLabel(self)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "LogoBea.png")
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Afbeelding niet gevonden:", image_path)
        pixmap = pixmap.scaled(150, 120)
        self.LogoBea.setPixmap(pixmap)
        self.LogoBea.setScaledContents(True)
        self.LogoBea.move(20, 20)

        self.inlog = QLabel("Vul uw inloggegevens in:", self)
        self.inlog.setFixedSize(300, 25)
        self.inlog.setVisible(True)
        self.inlog.move(200, 190)
        self.inlog.setStyleSheet("font-size: 19px; color: white; font-weight: bold;")

        self.gebruikersnaam = QLineEdit(self)
        self.gebruikersnaam.move(210, 235)
        self.gebruikersnaam.setFixedWidth(250)
        self.gebruikersnaam.setPlaceholderText("Gebruikersnaam")
        self.gebruikersnaam.setStyleSheet("font-size: 18px; color: white;")

        self.wachtwoord = QLineEdit(self)
        self.wachtwoord.setFixedWidth(250)
        self.wachtwoord.move(210, 270)
        self.wachtwoord.setPlaceholderText("Wachtwoord")
        self.wachtwoord.setEchoMode(QLineEdit.Password)
        self.wachtwoord.setStyleSheet("font-size: 18px; color: white;")

        self.adminch = QCheckBox("Ik ben docent op het BC", self)
        self.adminch.move(215, 300)
        self.adminch.setStyleSheet("font-size: 16px; color: white;")

        self.announce = QLabel("", self)
        self.announce.setFixedSize(300, 30)
        self.announce.move(200, 370)
        self.announce.setVisible(False)
        self.announce.setStyleSheet("font-size: 15px; color: white;")

        self.verstuur = QPushButton("Verstuur", self)
        self.verstuur.move(200, 335)
        self.verstuur.setFixedSize(150, 35)
        self.verstuur.setStyleSheet("font-size: 16px; font-weight: bold; background-color: lightgray;")
        self.verstuur.clicked.connect(self.login)

    def login(self):
        texmes = self.gebruikersnaam.text()
        if self.gebruikersnaam.text() != "" and self.wachtwoord.text() != "":
            if self.adminch.isChecked():
                db_path = os.path.join(
                   os.path.dirname(os.path.abspath(__file__)),
                    "database.db"
                )
                connect = sqlite3.connect(db_path)
                cursor = connect.cursor()
                cursor.execute("SELECT user, pass FROM adminlogin WHERE user=? AND pass=?",
                               (self.gebruikersnaam.text(), self.wachtwoord.text()))

                if cursor.fetchone():
                    print("Admin login validated")
                    self.window2 = HomeWindowAdmin(texmes)
                    self.window2.show()
                    self.close()
                    connect.close()
                    return
                else:
                    self.announce.setText("Onjuiste admin inloggegevens.")
                    self.announce.setVisible(True)
                connect.close()
            else:
                db_path = os.path.join(
                   os.path.dirname(os.path.abspath(__file__)),
                    "database.db"
                )
                connect = sqlite3.connect(db_path)
                cursor = connect.cursor()
                cursor.execute("SELECT user, pass FROM login WHERE user=? AND pass=?",
                               (self.gebruikersnaam.text(), self.wachtwoord.text()))

                if cursor.fetchone():
                    print("Login validated")
                    self.window2 = HomeWindow(texmes)
                    self.window2.show()
                    self.close()
                    connect.close()
                    return
                else:
                    self.announce.setText("Onjuiste inloggegevens.")
                    self.announce.setVisible(True)
                connect.close()
        else:           
            self.announce.setText("Vul alle velden in.")
            self.announce.setVisible(True)


class HomeWindowAdmin(QWidget):
    def __init__(self, texmes):
        super().__init__()

        self.setWindowTitle("WelkomPagina")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #4CAF50;")

        self.bovenform = QLabel("Chem2Go", self)
        self.bovenform.setFixedSize(700, 150)
        self.bovenform.setVisible(True)
        self.bovenform.move(0, 0)
        self.bovenform.setStyleSheet("background-color: #137827; " \
        "border: 2px solid black; font-size: 50px; font-weight: bold; color: white;")
        self.bovenform.setAlignment(Qt.AlignCenter)

        self.LogoBea = QLabel(self)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "LogoBea.png")
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Afbeelding niet gevonden:", image_path)
        pixmap = pixmap.scaled(150, 120)
        self.LogoBea.setPixmap(pixmap)
        self.LogoBea.setScaledContents(True)
        self.LogoBea.move(20, 20)
        self.LogoBea.setStyleSheet("background-color: #137827;")

        self.texmes = texmes
        self.inlog = QLabel(f"Welkom Admin {self.texmes}!", self)
        self.inlog.setFixedSize(250, 20)
        self.inlog.setVisible(True)
        self.inlog.move(230, 170)
        self.inlog.setStyleSheet("font-size: 19px; color: white; font-weight: bold;")

        self.voorraadzien = QPushButton("Voorraden", self)
        self.voorraadzien.move(120, 240)
        self.voorraadzien.setFixedSize(180, 180)
        self.voorraadzien.setStyleSheet(
            "QPushButton { font-size: 14px; font-weight: bold; " \
            "background-color: white; border: 2px dotted black; padding: 5px; }" \
            "QPushButton:hover { background-color: #F2F0ED; }")
        self.voorraadzien.clicked.connect(self.gaverder)

    def gaverder(self):
        self.window3 = VIBWindow()
        self.window3.show()
        self.close()


class HomeWindow(QWidget):
    def __init__(self, texmes):
        super().__init__()

        self.setWindowTitle("InlogPagina")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #4CAF50;")

        self.bovenform = QLabel("Chem2Go", self)
        self.bovenform.setFixedSize(700, 150)
        self.bovenform.setVisible(True)
        self.bovenform.move(0, 0)
        self.bovenform.setStyleSheet("background-color: #137827; " \
        "border: 2px solid black; font-size: 50px; font-weight: bold; color: white;")
        self.bovenform.setAlignment(Qt.AlignCenter)

        self.LogoBea = QLabel(self)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "LogoBea.png")
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Afbeelding niet gevonden:", image_path)
        pixmap = pixmap.scaled(150, 120)
        self.LogoBea.setPixmap(pixmap)
        self.LogoBea.setScaledContents(True)
        self.LogoBea.move(20, 20)
        self.LogoBea.setStyleSheet("background-color: #137827;")

        self.texmes = texmes
        self.inlog = QLabel(f"Welkom {self.texmes}!", self)
        self.inlog.setFixedSize(250, 20)
        self.inlog.setVisible(True)
        self.inlog.move(230, 170)
        self.inlog.setStyleSheet("font-size: 19px; color: white; font-weight: bold;")

        self.verder = QPushButton("Verder", self)
        self.verder.move(140, 270)
        self.verder.setFixedSize(130, 30)
        self.verder.setStyleSheet("font-size: 14px; font-weight: bold; background-color: lightgray;")
        self.verder.clicked.connect(self.gaverder)

    def gaverder(self):
        self.window3 = VIBWindow()
        self.window3.show()
        self.close()

class VIBWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VIBpagina")
        self.setFixedSize(700, 600)  
        self.setStyleSheet("background-color: #4CAF50;")  

        self.bovenform = QLabel("Chem2Go", self)
        self.bovenform.setFixedSize(700, 150)
        self.bovenform.setVisible(True)
        self.bovenform.move(0, 0)
        self.bovenform.setStyleSheet("background-color: #137827; " \
        "border: 2px solid black; font-size: 50px; font-weight: bold; color: white;")
        self.bovenform.setAlignment(Qt.AlignCenter)

        self.LogoBea = QLabel(self)
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, "LogoBea.png")
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Afbeelding niet gevonden:", image_path)
        pixmap = pixmap.scaled(150, 120)
        self.LogoBea.setPixmap(pixmap)
        self.LogoBea.setScaledContents(True)
        self.LogoBea.move(20, 20)
        self.LogoBea.setStyleSheet("background-color: #137827;")

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: black;")
        line.setFixedHeight(2)

        vib_title = QLineEdit("", self)
        vib_title.setVisible(True)
        vib_title.setPlaceholderText("VIBs zoeken...")
        vib_title.setTextMargins(10, 0, 0, 0)
        vib_title.setFixedSize(550, 50)
        vib_title.move(75, 180)
        vib_title.setStyleSheet("background-color: white; border: 2px solid black; font-size: 20px; font-weight: 500;")
        vib_title.textChanged.connect(lambda: self.tabelmaken(verlopenweergeven, table, vib_title.text()))

        verlopenweergeven = QCheckBox("Verlopen VIBs weergeven", self)
        verlopenweergeven.setStyleSheet("font-size: 16px; color: white;")
        verlopenweergeven.move(85, 230)
        verlopenweergeven.setChecked(False)
        verlopenweergeven.stateChanged.connect(lambda: self.tabelmaken(verlopenweergeven, table, vib_title.text()))

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setFixedSize(600, 430)
        table.setVisible(True)
        table.move(50, 260)
        table.setHorizontalHeaderLabels(["Naam", "Uitgever", "Verloopdatum"])
        table.setStyleSheet(
            "QTableWidget::item { background-color: white; border: 1px solid black; " \
            "font-size: 16px; font-style: italic; padding: 0 0 0 7px; }" \
            "QHeaderView::section { background-color: lightgray; border: 1px solid black; " \
            "font-size: 16px; }" \
            "QScrollBar { background: lightgray; }")
        table.setColumnWidth(0, 200)
        table.setColumnWidth(1, 200)
        table.setColumnWidth(2, 200)
        table.verticalHeader().setDefaultSectionSize(50)

        self.tabelmaken(verlopenweergeven, table, vib_title.text())

    def tabelmaken(self, verlopenweergeven, table, vib_title_text):
        db_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "database.db"
        )
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        if verlopenweergeven.isChecked() and vib_title_text.strip() == "":
            cursor.execute("SELECT stofnaam, stofuitgever, stofverloopdatum FROM VIBoverzicht WHERE stofverloopdatum IS NOT 'Verlopen'")
            rows = cursor.fetchall()
        elif vib_title_text.strip() != "":
            cursor.execute("SELECT stofnaam, stofuitgever, stofverloopdatum FROM VIBoverzicht WHERE stofnaam LIKE ?", ('%' + vib_title_text + '%',))
            rows = cursor.fetchall()
        else:
            cursor.execute("SELECT stofnaam, stofuitgever, stofverloopdatum FROM VIBoverzicht")
            rows = cursor.fetchall()
        
        connect.close()

        table.setRowCount(0)
        table.setRowCount(len(rows))

        for r, (naam, uitgever, verloop) in enumerate(rows):
            table.setItem(r, 0, QTableWidgetItem(naam))
            table.setItem(r, 1, QTableWidgetItem(uitgever))
            table.setItem(r, 2, QTableWidgetItem(verloop))

        table.setShowGrid(False)
        table.verticalHeader().setVisible(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
