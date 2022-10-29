# Only needed for access to command line arguments
import sys

import random

from PyQt5 import QtCore

# We import the PyQt5 classes that we need for the application
# from the QtWidgets module
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


###############
# MAIN WINDOW #
###############
# This is a pre-made widget which provides a lot of standard window 
# features you’ll make use of in your apps, including toolbars, menus, 
# a statusbar, dockable widgets and more.
class MainWindow(QMainWindow):
    def __init__(self):
        """!
        @brief Init MainWindow.
        """
        # If you want to create a custom window, the best approach is 
        # to subclass QMainWindow and then include the setup for the 
        # window in this __init__ block.

        super(MainWindow, self).__init__()

        # title and geometry
        self.setWindowTitle("GUI")
        width = 300
        height = 250
        self.setMinimumSize(width, height)

        self.initUI()

    #####################
    # GRAPHIC INTERFACE #
    #####################
    def initUI(self):
        """!
        @brief Set up the graphical interface structure.
        """
        # Define buttons
        self.plus_btn = QPushButton(
            text="+1",
            clicked=self.add_one
        )
        # alternatively, signals can be connected in this way
        # self.plus_btn.clicked.connect(self.add_one)
        self.minus_btn = QPushButton(
            text="-1",
            clicked=self.remove_one
        )
        # alternatively, signals can be connected in this way
        # self.plus_btn.clicked.connect(self.add_one)
        
        # Define lable to visualize numbers
        self.label_number = int(random.random()*100)
        self.display_label = QLabel(
            str(self.label_number),
            alignment=QtCore.Qt.AlignCenter
        )

        # layout
        button_hlay = QHBoxLayout()
        button_hlay.addWidget(self.plus_btn)
        button_hlay.addWidget(self.minus_btn)
        vlay = QVBoxLayout()
        vlay.addLayout(button_hlay)
        vlay.addWidget(self.display_label)
        widget = QWidget()
        widget.setLayout(vlay)
        #.setCentralWidget is a QMainWindow specific function that 
        # allows you to set the widget that goes in the middle of the window.
        self.setCentralWidget(widget)

    def add_one(self):
        """!
        @brief Add 1 to the number displayed in the label.
        """
        self.label_number = self.label_number+1
        self.display_label.setText(str(self.label_number))

    def remove_one(self):
        """!
        @brief Subtract 1 to the number displayed in the label.
        """
        self.label_number = self.label_number-1
        self.display_label.setText(str(self.label_number))


#############
#  RUN APP  #
#############
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([])
    # works too.
    app = QApplication(sys.argv)
    # Create a Qt widget, which will be our window.
    w = MainWindow()
    w.show() # IMPORTANT!!!!! Windows are hidden by default.
    # Start the event loop.
    sys.exit(app.exec_())

    # Your application won't reach here until you exit and the event
    # loop has stopped.