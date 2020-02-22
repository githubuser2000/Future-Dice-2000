import QtQuick 2.12
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.12

ColumnLayout {
    id : 'bla'
    RadioButton {
        checked: true
        text: qsTr("First")
    }
    RadioButton {
        text: qsTr("Second")
    }
    RadioButton {
        text: qsTr("Third")
    }
}
