from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect ui-widget to controller
        # if ui changes, it sends a signal to an slot on which we connect a controller class.
        # therefore we can recive the signal in the controller
        self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # Lambda to execute function with value
        self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        self._ui.pushButton_add.clicked.connect(lambda: self._main_controller.add_user(self._ui.lineEdit_name.text()))

        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # if model sends/emits a signal the ui gets notified
        self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        self._model.user_added.connect(self.on_list_changed)

        # set a default value
        self._main_controller.change_amount(42)

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox_amount.setValue(value)

    @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._ui.pushButton_reset.setEnabled(value)
    
    @pyqtSlot(str)
    def on_list_changed(self, value):
        self._ui.listWidget_names.addItem(value)