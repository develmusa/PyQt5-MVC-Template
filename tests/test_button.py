import unittest
import pytest
import pytest_xvfb

from PyQt5.QtCore import *

from src import button


def test_hello(qtbot):
    widget = button.SimpleButton()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.buttonA, Qt.LeftButton)

    assert widget.labelA.text() == "Changed"