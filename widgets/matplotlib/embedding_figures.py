"""
Imbedding a matplotlib figure in a PyQt5 widget.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
mpl.use('Qt5Agg')


class MainWindow(QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Create Figure
        x, y = list(range(10)), list(range(10))
        fig_widget = FigureCanvasQTAgg(figure=plt.Figure())
        ax = fig_widget.figure.add_subplot(111)
        ax.plot(x, y)

        # Embed figure in window
        self.setCentralWidget(fig_widget)

        # Window params
        self.resize(600, 400)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


