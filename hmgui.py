from hangman import *
import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel ,QPushButton,QLineEdit
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Hang man")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(600, 400, 900, 600)
        self.word = ["mango", "gorella" , "fucker"]
        self.wrong_guesses = 6
        self.answer = "aaaaaaaaaaa"
        self.hint = ["_"]* len(self.answer)

        self.l1 = QLabel(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}" ,self)
        self.l2 = QLabel(f"{display_hints(self.hint)}",self)
        
        self.t = QLineEdit("",self)
        self.b = QPushButton("start", self)
        self.InitGUI()

    def InitGUI(self):
        self.l1.setGeometry(0, 0, 900, 190)
        self.l2.setGeometry(0, 180, 900, 150)
        self.b.setGeometry(300, 500, 200, 100)
        self.t.setGeometry(200, 350, 400, 100)
       
        

        self.l1.setStyleSheet("font-size: 60px;"
                            "background-color: black;"
                            "Color : green")
        self.l2.setStyleSheet("font-size: 60px;"
                            "background-color: black;"
                            "Color : green")                     
        self.b.setStyleSheet("font-size: 20px;"
                            "background-color: silver;"
                            "Color : black")  

        self.l1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.l2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.t.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                         





def main():
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())

if __name__ == "__main__":  
    main()

