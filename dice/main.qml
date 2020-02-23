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
            objectName: "radiolayout"
            /*
            ButtonGroup {
                id: group
                buttons: repeaterradios.children
                objectName: "radiogroup"
                //onClicked: { MainWindow.getRadioBselected(MainWindow,button.text);
                onClicked:  console.log("clicked:",button.text)
            }*/
            Label {
                text: "lin"
                objectName: 'LRad'
                id : rade
                visible: false
            }
            Repeater {
                id: repeaterradios
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
                    //ButtonGroup.group: group
                    onClicked:  rade.text = text
                }
            }

        }
        Grid {
            columns: 2
            spacing: 2

            Switch {
                id: reverse_
                x: 90
                y: 119
                text: qsTr("Rückwärts")
                objectName: "reverse"
            }

            Switch {
                id: uniq
                x: 232
                y: 119
                text: qsTr("jeder Wurf passiert")
                objectName: "uniq"
            }
            Label {
                text: "Augen"
            }
            TextField {
                objectName: "augen"
                id : augen
                validator: IntValidator {bottom: 1; top: 10000000;}
                focus: true
                text: "3"
            }
            Label {
                text: "n"
            }
            TextField {
                objectName: "n"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
            }
            Label {

                text: "x"

            }
            TextField {
                objectName: "x"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
            }
            Label {
                text: "Wert an Stelle"

            }
            TextField {
                objectName: "y"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
            }
            Label {
                text: "Würfe"
            }
            TextField {
                objectName: "wuerfe"
                validator: IntValidator {bottom: 0; top: 10000000;}
                focus: true
                text: "3"
            }

            Button {
                id: bwuefelerstellen
                x: 196
                y: 383
                text: qsTr("Würfel erstellen")
                onClicked: MainWindow.wuerfelErstellen()
            }
            Button {
                id: bwuerfe
                x: 196
                y: 424
                text: qsTr("Würfeln")
                spacing: -3
                onClicked: MainWindow.wuerfeln2()
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

            ListView {
                model: scrollmodel
                highlight: Rectangle { color: "lightsteelblue" }
                highlightRangeMode: ListView.ApplyRange
                delegate: Text {
                    text: name
                }
            }
        }
        ColumnLayout {
            //anchors.fill: parent
            id: layoutZ


            Column {
                Repeater {
                    id: chk1
                    model: chkmodel1
                    objectName: "repeatercheck1"

                    CheckBox {
                        text : name
                        checked: checked_
                    }
                }
            }

        }

        ColumnLayout {
            //anchors.fill: parent
            id: layout5


            Column {

                Repeater {
                    id: chk2
                    model: chkmodel2
                    objectName: "repeatercheck2"

                    CheckBox {
                        text : name
                        checked: checked_

                    }
                }
            }

        }
        ColumnLayout {
            //anchors.fill: parent
            id: layout7



            Column {
                Repeater {
                    id: chk3
                    model: chkmodel3
                    objectName: "repeatercheck3"

                    CheckBox {
                        text : name
                        checked: checked_

                    }
                }
            }

        }
    }
}











/*##^## Designer {
    D{i:1;anchors_x:0;anchors_y:40}
}
 ##^##*/
