"""
Example of how a scroll bar can be embedded in a widget using QScrollArea. Most examples
online are limited to making the QMainWindow scrollable, and don't extend easily to adding
scrollable widgets to the QMainWindow layout.
"""

__all__ = ['VScrollableWidget']

from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout
from PyQt5.QtCore import Qt

class VScrollableWidget(QWidget):
    """
    Widget with an embedded scrollable area. Use by implementing setup_contents() method.
    """

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Create container for holding widget contents.
        self.contents = QWidget()
        self.setup_contents()

        # Create scrollable area and add contents widget
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.contents)

        # Add scrollable area to "self" widget
        layout = QVBoxLayout()  # Note: type of layout here unimportant as only one widget added.
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

    def setup_contents(self):
        """
        To implement:
        (1) create layout of component widgets.
        (2) create components and add to layout.
        (3) set layout to the self.contents widget.
        """
        raise NotImplementedError()


# ------- #
# Example #
# ------- #

if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QHBoxLayout


    class ExampleWidget(VScrollableWidget):
        """Scrollable list of numbers"""

        def __init__(self, parent=None, n=50, *args, **kwargs):
            self.n = n  # Length of number list
            super().__init__(parent, *args, **kwargs)

        def setup_contents(self):
            # Construct components and add them to a layout
            layout = QVBoxLayout()
            for i in range(self.n):
                layout.addWidget(QLabel(f'{i}'))

            # Set layout to container widget.
            self.contents.setLayout(layout)


    class MainWindow(QMainWindow):
        """Simple ui with two scrollable lists."""
        def __init__(self, parent=None):
            super().__init__(parent)

            container = QWidget()
            layout = QHBoxLayout()
            layout.addWidget(ExampleWidget(self, 50))  # Add multiple scrollers
            layout.addWidget(ExampleWidget(self, 100))
            container.setLayout(layout)
            self.setCentralWidget(container)


    # ----------- #
    # Run Program #
    # ----------- #
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 480)
    window.show()
    sys.exit(app.exec_())
