import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.12


Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    GridLayout {
        anchors.fill: parent
        columns: 3

        Label {
            text: ""
        }
        Label {
            objectName: "foo_object"
            text: "nichts"
        }
        Label {
            text: ""
        }


        ColumnLayout {
            Repeater {
                model: radiomodel
                objectName: "radios"
                RadioButton {
                    checked: radiomodel.checked
                    //text: qsTr("First")
                    text: radiomodel.text
                    objectName: radiomodel.text
                }
            }

        }
        Grid {
            columns: 2
            spacing: 2
            Label {
                text: "Label"
            }
            TextField {
                validator: IntValidator {bottom: 11; top: 31;}
                focus: true
            }
            Label {
                text: "Label"
            }
            TextField {
                validator: IntValidator {bottom: 11; top: 31;}
                focus: true
            }
            Label {
                text: "Label"
            }
            TextField {
                validator: IntValidator {bottom: 11; top: 31;}
                focus: true
            }
            Label {
                text: "Label"
            }
            TextField {
                validator: IntValidator {bottom: 11; top: 31;}
                focus: true
            }
            Label {
                text: "Label"
            }
            TextField {
                validator: IntValidator {bottom: 11; top: 31;}
                focus: true
            }

        }
        ListView {
            width: 180; height: 200

            model: ContactModel {}
            delegate: Text {
                text: name + ": " + number
            }
        }
        ColumnLayout {
            //anchors.fill: parent
            id: layout

            ButtonGroup { id: radioA }
            Column {

                CheckBox {
                    id: parentBox1
                    text: qsTr("Parent")
                    //checkState: childGroup.checkState
                }

                CheckBox {
                    checked: true
                    text: qsTr("Child 1")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioA
                }

                CheckBox {
                    text: qsTr("Child 2")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioA
                }
            }
        }
        ColumnLayout {
            //anchors.fill: parent
            id: layout5

            ButtonGroup { id: radioB }
            Column {

                CheckBox {
                    id: parentBox2
                    text: qsTr("Parent")
                    //checkState: childGroup.checkState
                }

                CheckBox {
                    checked: true
                    text: qsTr("Child 1")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioB
                }

                CheckBox {
                    text: qsTr("Child 2")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioB
                }
            }
        }
        ColumnLayout {
            //anchors.fill: parent
            id: layout7

            ButtonGroup { id: radioC }
            Column {

                CheckBox {
                    id: parentBox3
                    text: qsTr("Parent")
                    //checkState: childGroup.checkState
                }

                CheckBox {
                    checked: true
                    text: qsTr("Child 1")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioC
                }

                CheckBox {
                    text: qsTr("Child 2")
                    leftPadding: indicator.width
                    ButtonGroup.group: radioC
                }
            }
        }
    }
}


/*##^## Designer {
    D{i:1;anchors_x:0;anchors_y:40}
}
 ##^##*/
