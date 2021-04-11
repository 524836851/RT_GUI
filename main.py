import sys
 
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow

import MainWindow 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MainWindow.MyMain()
    MyWindow.show()
    sys.exit(app.exec_())
 