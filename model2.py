from PyQt5.QtCore import QAbstractListModel, Qt, pyqtSignal, pyqtSlot, QModelIndex, QModelIndex

class PersonModel(QAbstractListModel):

    Name = Qt.UserRole + 1
    Checked = Qt.UserRole + 2

    personChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.persons = [
            #{'name': 'jon', 'checked_': True},
            #{'name': 'jane', 'checked_': False}
        ]

    def data(self, QModelIndex, role):
        row = QModelIndex.row()
        if role == self.Name:
            return self.persons[row]["name"]
        if role == self.Checked:
            return self.persons[row]["checked_"]

    def rowCount(self, parent=None):
        return len(self.persons)

    def roleNames(self):
        return {
            Qt.UserRole + 1: b'name',
            Qt.UserRole + 2: b'checked_'
        }

    @pyqtSlot()
    def addData(self):
        self.beginResetModel()
        self.persons = self.persons.append({'name': 'peter', 'checked_': False})
        self.endResetModel()
        print(self.persons)

    @pyqtSlot()
    def editData(self):
        print(self.model.persons)
    @pyqtSlot(int, str, int)
    def insertPerson(self, row, name, checked_):
        self.beginInsertRows(QModelIndex(), row, row)
        self.persons.insert(row, {'name': name, 'checked_': checked_})
        self.endInsertRows()
