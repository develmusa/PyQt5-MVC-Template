from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # Takes Signal from UI
    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'even'

        # calculate button enabled state
        self._model.enable_reset = True if value else False

    @pyqtSlot(str)
    def add_user(self, value):
        self._model.add_user(value)
        # calculate button enabled state
        #if(self._model.users.count > 0):
        #    self._model.enable_del_user = True if value else False

    @pyqtSlot(int)
    def delete_user(self, value):
        self._model.delete_user(value)
        # calculate button enabled state
        #if(self._model.users.count > 0):
        #    self._model.enable_del_user = True if value else False