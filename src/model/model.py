from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):

    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)
    users_changed = pyqtSignal(list)

    @property
    def users(self):
        return self._users


    def add_user(self, value):
        self._users.append(value)
        self.users_changed.emit(self._users)

    def delete_user(self, value):
        del self._users[value]
        self.users_changed.emit(self._users)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._amount = 0
        self._even_odd = ''
        self._enable_reset = False

        self._users = ["hans"]