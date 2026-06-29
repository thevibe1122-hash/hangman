from hangman import *
import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel ,QPushButton,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import time
import random


class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Hang man")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(600, 350, 900, 600)
        self.word = ["mango", "gorella" , "fucker"]
        self.wrong_guesses = 0
        self.answer = random.choice(self.word)
        self.hint = ["_"]* len(self.answer)
        self.text = ""
        self.guessed = set()

        self.l1 = QLabel(f" {display_man(6,0)} \n  {display_man(6,1)} \n  {display_man(6,2)}" ,self)
        self.l2 = QLabel(f"{display_hints(self.hint)}",self)
        self.l4 = QLabel("hang man",self)
        
        self.t = QLineEdit("",self)
        self.b = QPushButton("start", self)
        self.InitGUI()

    def InitGUI(self):
        self.l1.setGeometry(0, 100, 900, 190)
        self.l2.setGeometry(0, 280, 900, 150)
        self.l4.setGeometry(0, 0, 900, 100)

        self.b.setGeometry(630, 440, 200, 100)
        self.t.setGeometry(200, 440, 400, 100)
        self.t.setMaxLength(1)
        

        self.l1.setStyleSheet("font-size: 60px;"
                            "background-color: black;"
                            "Color : green")
        self.l2.setStyleSheet("font-size: 60px;"
                            "background-color: black;"
                            "Color : green")   
        self.l4.setStyleSheet("font-size: 60px;"
                            "background-color: silver;"
                            "Color : black")                    
        self.b.setStyleSheet("font-size: 20px;"
                            "background-color: silver;"
                            "Color : black")  
        self.t.setStyleSheet("font-size: 60px;"
                            "background-color: silver;"
                            "Color : black")  
        
        self.t.setEnabled(False)

        self.l1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.l2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.l4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.t.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.b.clicked.connect(self.onClick)

    def game_play(self):

        if self.text  in self.guessed:
            self.l4.setText(f'{self.text} is already guessed')
            self.t.clear()
            return
        
        else:
            self.guessed.add(self.text)


        if self.text in self.answer:
            for i in range(len(self.answer)) :
                if self.answer[i]==self.text:
                    self.hint[i] = self.text
                    self.l4.setText(f"{self.text} is right")
                    self.l2.setText(f"{display_hints(self.hint)}")
                    self.t.clear()

        else:
            self.wrong_guesses +=1
            self.l4.setText(f"{self.text} is wrong")
            self.l1.setText(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}")
            self.t.clear()

        if "_" not in self.hint:
            self.l1.setText(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}")
            self.l2.setText(f"{display_answer(self.answer)}")
            self.wrong_guesses == 6 
            self.l4.setText("you win")
            self.b.setText("play again")
            self.t.setEnabled(False)
            self.t.clear()
            return

        elif self.wrong_guesses >= 6:
            self.l1.setText(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}")
            self.l2.setText(f"{display_answer(self.answer)}")
            self.l4.setText("you lose")
            self.b.setText("play again")
            self.t.setEnabled(False)
            self.t.clear()
        


        



        
        
        

    def onClick(self):
        self.text= self.t.text()
        self.b.setText("Submit")
        self.t.clear()
        self.t.setEnabled(True)
        self.l1.setText(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}")
        
        
        if self.wrong_guesses == 6:
            self.wrong_guesses = 0 
            self.answer = random.choice(self.word)
            self.hint = ["_"]* len(self.answer)
            self.t.clear()
            self.t.setEnabled(True)
            self.l1.setText(f" {display_man(self.wrong_guesses,0)} \n  {display_man(self.wrong_guesses,1)} \n  {display_man(self.wrong_guesses,2)}")
            self.l2.setText(f"{display_hints(self.hint)}")
            self.l4.setText("hang man")
            self.b.setText("Submit")
        else:
            self.game_play()

        



        
       

        

                         





def main():
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())

if __name__ == "__main__":  
    main()

