import QtQuick 2.8
import QtQuick.Window 2.8
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.8


Window {
    visible: true
    //width: 700
    //height: 580
    width: haupt.width + gridcheckboxes.width
    height: haupt.height + gridpartentradios.height
    title: qsTr("Dice Future 2000")
    id : win


    GridLayout {
        //anchors.fill: parent
        columns: 3
        anchors.leftMargin: 20
        anchors.topMargin: 20
        anchors.rightMargin: 20

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

            Switch {
                id: reverse_
                x: 90
                y: 119
                text: qsTr("invert")
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

                text: qsTr("invert Z")
                objectName: "reverse2"
            }
            Label {
                text: " "
            }
            Label {
                text: "   Augen"
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
                text: "   n"
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
                text: "n<sub>2</sub>"
                textFormat: Text.RichText
            }

            TextField {
                objectName: "n2"
                id : n2
                enabled: false
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "   x"
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
                textFormat: Text.RichText
                text: "x<sub>2</sub>"
            }

            TextField {
                objectName: "x2"
                id : x2
                enabled: false
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Label {
                text: "   y"

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
                text: "y<sub>2</sub>"
                textFormat: Text.RichText
            }

            TextField {
                objectName: "y2"
                id : y2
                enabled: false
                validator: DoubleValidator {bottom: 0.1; top: 100000000000;}
                focus: true
                text: "3"
                width: 50
                horizontalAlignment: Text.AlignRight

            }
            Button {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                id: bwuefelerstellen
                x: 196
                y: 383
                text: qsTr("Würfel erstellen")
                antialiasing: true
                onClicked: MainWindow.wuerfelErstellen()
                background: Rectangle {
                    implicitWidth: 100
                    implicitHeight: 40
                    color: bwuefelerstellen.down ? "#d6d6d6" : "#f6f6f6"
                    border.color: "#26282a"
                    border.width: 2
                    radius: 13
                }

            }
            Label {
                text: " "
                //textFormat: Text.RichText
            }
            Button {
                anchors.leftMargin: 20
                anchors.rightMargin: 20
                id: bwuerfe
                x: 196
                y: 424
                text: qsTr("Würfeln")
                antialiasing: true
                spacing: -3
                onClicked: MainWindow.wuerfeln2()
                background: Rectangle {
                    implicitWidth: 100
                    implicitHeight: 40
                    color: bwuerfe.down ? "#d6d6d6" : "#f6f6f6"
                    border.color: "#26282a"
                    border.width: 2
                    radius: 13
                }
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
            id : gridpartentradios

            transformOrigin: Item.TopLeft
            columns: 1
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            Switch {
                id: gewicht
                x: 90
                y: 119
                text: qsTr("gezinkt")
                objectName: "gewicht"
                //repeaterradios2
                onToggled: {
                    for (var i = 0; i < chk2layout.children.length; i++)
                        chk2layout.children[i].enabled = gewicht.position;
                    for (var i = 0; i < radio2grid.children.length; i++)
                        radio2grid.children[i].enabled = gewicht.position;
                    y2.enabled = gewicht.position;
                    x2.enabled = gewicht.position;
                    n2.enabled = gewicht.position;

                }
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
                    id : radio1grid
                    Label {
                        text: "Wert"
                        objectName: 'L1'
                        id : l1
                    }
                    Repeater {
                        id: repeaterradios
                        model: radiomodel1
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
                            onToggled:  {
                                rade.text = text;
                                lCheck0.anArray[0] = text === 'kombi' ? checked : false
                                console.log("x",lCheck0.anArray[0]);
                                console.log("y",lCheck0.anArray[1]);
                                if (lCheck0.anArray[0] || lCheck0.anArray[1])
                                    for (var i = 0; i < chk3layout.children.length; i++)
                                        chk3layout.children[i].enabled = true;
                                else
                                    for (var i = 0; i < chk3layout.children.length; i++)
                                        chk3layout.children[i].enabled = false;
                            }

                        }
                    }
                }
                GridLayout {
                    transformOrigin: Item.TopLeft
                    columns: 1
                    id : radio2grid

                    Label {
                        text: "gezinkt"
                        objectName: 'L2'
                        id : l2
                    }
                    Repeater {
                        id: repeaterradios2
                        model: radiomodel2
                        objectName: "radios2"
                        RadioButton {

                            enabled : false
                            Layout.preferredHeight: 15
                            indicator.height: 15
                            indicator.width: 15
                            checked: checked_
                            //text: qsTr("First")
                            text: name
                            objectName: name
                            //ButtonGroup.group: group
                            ButtonGroup.group: radioGroup2
                            onToggled:  {
                                rade.text = text;
                                lCheck0.anArray[1] = text === 'kombi' ? checked : false

                                if (lCheck0.anArray[0] || lCheck0.anArray[1])
                                    for (var i = 0; i < chk3layout.children.length; i++)
                                        chk3layout.children[i].enabled = true;
                                else
                                    for (var i = 0; i < chk3layout.children.length; i++)
                                        chk3layout.children[i].enabled = false;
                            }

                        }
                    }
                }
            }
        }
        Item { Layout.fillWidth: true }

        ScrollView {
            id: scrollView
            objectName: 'scrollView'
            //x: 487
            //y: 174
            width: listView.height
            height: listView.height
            antialiasing: true
            transformOrigin: Item.TopLeft
            //Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.fillHeight: true
            //clip: true
            //spacing: 2
            //padding: -2
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn
            contentHeight: listView.height
            contentWidth: listView.width

            ListView {
                id: listView
                //implicitHeight: scrollView.height
                //implicitWidth: scrollView.width
                width: scrollView.width
                height: scrollView.height
                Layout.fillWidth: true
                Layout.fillHeight: true
                antialiasing: true
                transformOrigin: Item.TopLeft
                //anchors.fill: parent
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
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            transformOrigin: Item.TopLeft
            id : gridcheckboxes
            Layout.fillWidth: true

            columns: 3
            Label {
                text: "LCheck1"
                objectName: '_LCheckA_'
                id : lCheck0
                visible: false
                property var anArray: new Array(2).fill(false);
            }
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
                id : chk2layout
                Repeater {
                    id: chk2
                    model: chkmodel2
                    objectName: "repeatercheck2"

                    CheckBox {
                        enabled : false
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
                id : chk3layout
                Repeater {
                    id: chk3
                    model: chkmodel3
                    objectName: "repeatercheck3"

                    CheckBox {
                        id : id_
                        enabled : false
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
