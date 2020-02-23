import QtQuick 2.8
import QtQuick.Window 2.8
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.8


Window {
    visible: true
    width: 700
    height: 580
    title: qsTr("Dice Future 2000")
    id : win


    GridLayout {
        //anchors.fill: parent
        columns: 4
        anchors.leftMargin: 20
        anchors.topMargin: 20
        anchors.rightMargin: 20
        anchors.left: win.right
        anchors.top: win.top
/*        Label {
            text: " "
        }*/
        Grid {
            id: haupt
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            transformOrigin: Item.TopLeft
            columns: 4
            spacing: 10
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.topMargin: 20
            //anchors.fill: parent
            anchors.left: win.right
            anchors.top: win.top



            Switch {
                id: reverse_
                x: 90
                y: 119
                text: qsTr("umgekehrt")
                objectName: "reverse"
            }

            Switch {
                id: uniq
                x: 232
                y: 119
                text: qsTr("uniq")
                objectName: "uniq"
            }


            Switch {
                id: reverse2_
                x: 90
                y: 119
                text: qsTr("umgekehrt2")
                objectName: "reverse2"
            }
            Label {
                text: " "
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
                width: 50
                horizontalAlignment: Text.AlignRight
            }
            Label {
                text: "Würfe"
            }
            TextField {
                objectName: "wuerfe"
                id : wuerfe
                validator: IntValidator {bottom: 1; top: 10000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "n"
            }
            TextField {
                objectName: "n"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight
            }
            Label {
                text: "n2"
            }

            TextField {
                objectName: "n2"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "x"
            }
            TextField {
                objectName: "x"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "x2"
            }

            TextField {
                objectName: "x2"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "Wert an Stelle"

            }
            TextField {
                objectName: "y"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "Wert 2    "
            }

            TextField {
                objectName: "y2"
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

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
        ButtonGroup {
            id: radioGroup
        }
        ButtonGroup {
            id: radioGroup2
        }
        Grid {
            anchors.leftMargin: 20
            anchors.rightMargin: 20

            transformOrigin: Item.TopLeft
            columns: 1
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            Switch {
                id: gewicht
                x: 90
                y: 119
                text: qsTr("gezinkt")
                objectName: "gewicht"
            }
            GridLayout {
                anchors.leftMargin: 20
                anchors.rightMargin: 20

                transformOrigin: Item.TopLeft
                columns: 2
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
                Label {
                    text: "lin"
                    objectName: 'LRad2'
                    id : rade2
                    visible: false
                }



                GridLayout {
                    transformOrigin: Item.TopLeft
                    columns: 1
                    Label {
                        text: "Wert"
                        objectName: 'L1'
                        id : l1
                    }
                    Repeater {
                        id: repeaterradios
                        model: radiomodel
                        objectName: "radios"
                        RadioButton {
                            Layout.preferredHeight: 15
                            indicator.height: 15
                            indicator.width: 15
                            checked: checked_
                            //text: qsTr("First")
                            text: name
                            objectName: name
                            ButtonGroup.group: radioGroup
                            onClicked:  rade.text = text
                        }
                    }
                }
                GridLayout {
                    transformOrigin: Item.TopLeft
                    columns: 1

                    Label {
                        text: "gezinkt"
                        objectName: 'L2'
                        id : l2
                    }
                    Repeater {
                        id: repeaterradios2
                        model: radiomodel
                        objectName: "radios2"
                        RadioButton {
                            Layout.preferredHeight: 15
                            indicator.height: 15
                            indicator.width: 15
                            checked: checked_
                            //text: qsTr("First")
                            text: name
                            objectName: name
                            //ButtonGroup.group: group
                            onClicked:  rade2.text = text
                            ButtonGroup.group: radioGroup2
                        }
                    }
                }
            }
        }
        Item { Layout.fillWidth: true }



        //anchors.fill: parent
        id: layoutZ
        ScrollView {
            id: scrollView
            objectName: 'scrollView'
            //x: 487
            //y: 174
            width: 200
            height: 100
            //Layout.fillHeight: true
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

        GridLayout {
            anchors.leftMargin: 20
            anchors.rightMargin: 20

            transformOrigin: Item.TopLeft

            columns: 3

            Label {
                text: "LCheck1"
                objectName: '_LCheck1_'
                id : lCheck1
                visible: false
                property var anObject: { "lin": true }
            }
            Label {
                text: "LCheck2"
                objectName: '_LCheck2_'
                id : lCheck2
                visible: false
                property var anObject: { "lin": true }
            }
            Label {
                text: "LCheck3"
                objectName: '_LCheck3_'
                id : lCheck3
                visible: false
                property var anObject: { "lin": true }
            }


            ColumnLayout {
                Repeater {
                    id: chk1
                    model: chkmodel1
                    objectName: "repeatercheck1"

                    CheckBox {
                        Layout.preferredHeight: 15
                        indicator.height: 15
                        indicator.width: 15
                        text : name
                        objectName: 'chk1_'+name
                        checked: checked_
                        onCheckedChanged: lCheck1.anObject[text]=checked

                    }
                }
            }
            ColumnLayout {
                Repeater {
                    id: chk2
                    model: chkmodel2
                    objectName: "repeatercheck2"

                    CheckBox {
                        Layout.preferredHeight: 15
                        indicator.height: 15
                        indicator.width: 15
                        text : name
                        checked: checked_
                        onCheckedChanged: lCheck2.anObject[text]=checked
                    }
                }
            }
            ColumnLayout {
                Repeater {
                    id: chk3
                    model: chkmodel3
                    objectName: "repeatercheck3"

                    CheckBox {
                        Layout.preferredHeight: 15
                        indicator.height: 15
                        indicator.width: 15
                        text : name
                        checked: checked_
                        onCheckedChanged: lCheck3.anObject[text]=checked

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
