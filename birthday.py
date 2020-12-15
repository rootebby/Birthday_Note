from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QCalendarWidget,
    QPushButton,
    QTextEdit,
    QCalendarWidget
)

import sys





class Ebby(QWidget):
    def __init__(self):
        super().__init__()

        self.root()

    def root(self):
        self.calender = QCalendarWidget()

        # programın solunda
        self.text = QTextEdit("")

        # programın sağında
        self.name_text = QLabel("Name")
        self.name = QLineEdit("")
        self.surname_text = QLabel("Surname")
        self.surname = QLineEdit("")
        self.gift_text = QLabel("Gift")
        self.gift = QLineEdit("")
        self.date_text  = QLabel("Date")
        self.date = QLineEdit("")

        # butonlar
        self.save = QPushButton("Save")
        self.clear = QPushButton("Clear")
        self.update = QPushButton("Update")

        vbox_c = QVBoxLayout()
        vbox_l = QVBoxLayout()
        vbox_r = QVBoxLayout()


        vbox_c.addWidget(self.calender)

        hbox_main = QHBoxLayout()
        hbox_r1 = QHBoxLayout()
        hbox_r2 = QHBoxLayout()
        hbox_r3 = QHBoxLayout()
        hbox_r4 = QHBoxLayout()
        hbox_r5 = QHBoxLayout()

        vbox_l.addWidget(self.text)

        hbox_r1.addStretch()
        hbox_r1.addStretch()
        hbox_r1.addStretch()
        hbox_r1.addWidget(self.name_text)
        hbox_r1.addStretch()
        hbox_r1.addWidget(self.name)

        hbox_r2.addStretch()
        hbox_r2.addStretch()
        hbox_r2.addStretch()
        hbox_r2.addWidget(self.surname_text)
        hbox_r2.addStretch()
        hbox_r2.addWidget(self.surname)

        hbox_r3.addStretch()
        hbox_r3.addStretch()
        hbox_r3.addStretch()
        hbox_r3.addWidget(self.gift_text)
        hbox_r3.addStretch()
        hbox_r3.addWidget(self.gift)


        hbox_r4.addStretch()
        hbox_r4.addStretch()
        hbox_r4.addStretch()
        hbox_r4.addWidget(self.date_text)
        hbox_r4.addStretch()
        hbox_r4.addWidget(self.date)

        hbox_r5.addWidget(self.clear)
        hbox_r5.addWidget(self.save)
        hbox_r5.addWidget(self.update)

        vbox_r.addLayout(hbox_r1)
        vbox_r.addLayout(hbox_r2)
        vbox_r.addLayout(hbox_r3)
        vbox_r.addLayout(hbox_r4)
        vbox_r.addLayout(hbox_r5)

        hbox_main.addLayout(vbox_c)
        hbox_main.addStretch()
        hbox_main.addLayout(vbox_l)
        hbox_main.addLayout(vbox_r)

        self.setLayout(hbox_main)
        
        self.update.clicked.connect(self.update_all)
        self.clear.clicked.connect(self.clear_out)
        self.save.clicked.connect(self.save_birth)
        self.setWindowTitle("Birthday Database")
        self.show()

    def save_birth(self):
        text = (f"""
Name : {self.name.text()}
Surname : {self.surname.text()}
Date : {self.date.text()}
Gift : {self.gift.text()}
        """)

        with open("birthday.txt","a",encoding="UTF-8") as file:
            file.write(str(text))
            self.text.setText(text)

    def clear_out(self):
        self.name.clear()
        self.surname.clear()
        self.gift.clear()
        self.date.clear()

    def update_all(self):
        empty_list = ""
        with open("birthday.txt","r",encoding="UTF-8") as file:
            for word in file:
                empty_list += str(word)
        self.text.setText(str(empty_list))
        


def main():
    app = QApplication(sys.argv)
    ebby = Ebby()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()