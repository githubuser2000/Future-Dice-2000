import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.12


Window {
    visible: true
    width: 840
    height: 680
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
                    Layout.preferredHeight: 20
                    indicator.height: 20
                    indicator.width: 20
                    checked: checked_
                    //text: qsTr("First")
                    text: name
                    objectName: name
                }
            }

        }
        Grid {
            columns: 2
            spacing: 2
            Label {
                text: "Augen"
            }
            TextField {
                objectName: "augen"
                validator: IntValidator {bottom: 1; top: 10000000;}
                focus: true
            }
            Label {
                text: "n"
            }
            TextField {
                objectName: "n"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
            }
            Label {

                text: "x"
            }
            TextField {
                objectName: "x"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
            }
            Label {
                text: "Wert an Stelle"
            }
            TextField {
                objectName: "y"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
            }
            Label {
                text: "Würfe"
            }
            TextField {
                objectName: "wuerfe"
                validator: IntValidator {bottom: 0; top: 10000000;}
                focus: true
            }

            Button {
                id: wuefelerstellen
                x: 196
                y: 383
                text: qsTr("Würfel erstellen")
                onClicked: MainWindow.wuerfelErstellen()
            }
            Button {
                id: wuerfe
                x: 196
                y: 424
                text: qsTr("Würfeln")
                spacing: -3
            }

        }
        ScrollView {
            id: scrollView
            objectName: 'scrollView'
            x: 487
            y: 174
            width: 200
            height: 200
            Layout.fillHeight: true
            Layout.fillWidth: true
            clip: true
            spacing: 2
            padding: -2
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn
            /*
            Repeater {
                model: scrollmodel
                objectName: "scrollrepeater"
                Label {
                    text: "ABC"
                    font.pixelSize: 224
                }
                Label {
                    text: "ABC"
                    font.pixelSize: 224
                }
            }*/
            ListView {
                model: scrollmodel
                delegate: ItemDelegate {
                    text: name
                }
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
