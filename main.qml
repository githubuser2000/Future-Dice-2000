import QtQuick 2.8
import QtQuick.Window 2.8
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.8
import Qt.labs.platform 1.1


Window {
    visible: true
    //width: haupt.width + gridcheckboxes.width
    width: haupt1.width
    title: qsTr("Future-Dice-2000")
    id : win
    onVisibleChanged: {
        height = haupt.height + scrollView.height + wuerfflaechNam.height + 12;
    }
    SystemTrayIcon {
        visible: true
        icon.source: "wuerfel.png"
        tooltip : qsTr("Future-Dice-2000")
        id : tray
        menu: Menu {
            MenuItem {
                text: qsTr("Würfeln")
                onTriggered: MainWindow.wuerfeln2()
            }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
        onActivated: {
            win.visible = ! win.visible
        }
    }
    onAfterRendering: {
        scrollView.height = height -haupt.height - wuerfflaechNam.height - 12;
        height = haupt.height + scrollView.height + wuerfflaechNam.height + 12;
    }
    Component.onCompleted: {
        setX(Screen.width / 2 - width / 2);
        setY(Screen.height / 2 - height / 2);
    }
    GridLayout {
        id: haupt1
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
                onClicked: MainWindow.uniq()
            }
            Switch {
                id: reverse2_
                x: 90
                y: 119

                text: qsTr("invert Z")
                objectName: "reverse2"
            }
            Switch {
                id: nega_
                text: qsTr("+  ")
                objectName: "nega_"
                width : 100
                onCheckedChanged: {
                    medi_.enabled = checked;
                    if (checked)
                        text = qsTr('+-')
                    else
                        text = qsTr('+')
                }
            }
            Label {
                text: qsTr("   Augen")
            }
            TextField {
                objectName: "augen"
                id : augen
                validator: IntValidator {bottom: 2; top: 10000000;}
                focus: true
                text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight

                onFocusChanged: {
                    if (text == "" ) text = Number("2");
                    if (parseInt(text,10) <2) text = 2;
                    if (parseInt(x.text,10) > parseInt(text,10)) x.text = text;
                    if (parseInt(x2.text,10) > parseInt(text,10)) x2.text = text;

                }
                onTextChanged: {
                    if (parseInt(text,10) <2) text = 2;
                    if (! x === null)
                        if (parseInt(x.text,10) > parseInt(text,10)) x.text = text;
                    if (! x2 === null)
                        if (parseInt(x2.text,10) > parseInt(text,10)) x2.text = text;

                }
                onTextEdited: {
                    if (parseInt(text,10) <2) text = 2;
                    if (parseInt(x.text,10) > parseInt(text,10)) x.text = text;
                    if (parseInt(x2.text,10) > parseInt(text,10)) x2.text = text;
                }
            }
            Label {
                text: qsTr("Würfe")
            }
            TextField {
                objectName: "wuerfe"
                id : wuerfe
                validator: IntValidator {bottom: 1; top: 10000000;}
                focus: true
                text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight
                onFocusChanged: {
                    if (text == "" ) text = "0";
                }
            }
            Label {
                text: "   n"
            }
            TextField {
                objectName: "n"
                validator: RegExpValidator { regExp: /^[0-9]+[\.,]?[0-9]*$/ }
                focus: true
                text: Number("3")
                property real nn: parseFloat(text);
                width: 50
                horizontalAlignment: Text.AlignRight
                onFocusChanged: {
                    if (text == "" || parseFloat(text,10) === 0 ) text = Number("1");
                    nn = parseFloat(text.replace(",","."),10)
                }
            }
            Label {
                text: "n<sub>2</sub>"
                textFormat: Text.RichText
            }
            TextField {
                objectName: "n2"
                id : n2
                enabled: false
                validator: RegExpValidator { regExp: /^[0-9]+[\.,]?[0-9]*$/ }
                focus: true
                text: Number("3")
                property real nn: parseFloat(text);
                width: 50
                horizontalAlignment: Text.AlignRight
                onFocusChanged: {
                    if (text == "" || parseInt(text,10) === 0 ) text = Number("1");
                    nn = parseFloat(text.replace(",","."),10)
                }
            }
            Label {
                text: "   x"
            }
            TextField {
                id : x
                objectName: "x"
                validator: RegExpValidator { regExp: /^[1-9]+[0-9]*$/ }
                focus: true
                //text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight

                onFocusChanged: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text
                    if (text == "" ) text = Number("1");
                }
                onTextChanged: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text
                }
                onTextEdited: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text

                }
            }
            Label {
                textFormat: Text.RichText
                text: "x<sub>2</sub>"
            }

            TextField {
                objectName: "x2"
                id : x2
                enabled: false
                validator: RegExpValidator { regExp: /^[1-9]+[0-9]*$/ }
                focus: true
                text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight
                onFocusChanged: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text
                    if (text == "" ) text = Number("1");
                }
                onTextChanged: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text
                }
                onTextEdited: { if (parseInt(text,10) > parseInt(augen.text,10)) text = augen.text
                }
            }
            Label {
                text: "   y"

            }
            TextField {
                objectName: "y"
                validator: RegExpValidator { regExp: /^[0-9]+[\.,]?[0-9]*$/ }
                focus: true
                text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight
                property real nn: parseFloat(text);
                onFocusChanged: {
                    if (text == "" ) text = Number("1");
                    nn = parseFloat(text.replace(",","."),10)
                }

            }
            Label {
                text: "y<sub>2</sub>"
                textFormat: Text.RichText
            }
            TextField {
                objectName: "y2"
                id : y2
                enabled: false
                validator: RegExpValidator { regExp: /^[0-9]+[\.,]?[0-9]*$/ }
                focus: true
                text: Number("3")
                width: 50
                horizontalAlignment: Text.AlignRight
                property real nn: parseFloat(text);
                onFocusChanged: {
                    if (text == "" ) text = Number("1");
                    nn = parseFloat(text.replace(",","."),10)
                }
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
        GridLayout{
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            id : gridpartentradios

            transformOrigin: Item.TopLeft
            columns: 1
            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
            Grid
            {
                anchors.leftMargin: 20
                anchors.rightMargin: 20

                transformOrigin: Item.TopLeft
                columns: 2
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
                        wuerfflaechNam.changed();
                    }
                }
                Button {
                    anchors.leftMargin: 20
                    anchors.rightMargin: 20
                    id: language
                    text: qsTr("")
                    antialiasing: true
                    spacing: -3
                    onClicked: MainWindow.changeLanguage()
                    background: Image {
                        /*
                        implicitWidth: 100
                        implicitHeight: 40
                        color: bwuerfe.down ? "#d6d6d6" : "#f6f6f6"
                        border.color: "#26282a"
                        border.width: 2
                        radius: 13*/
                        source: 'deutschland.png'
                        id: langimg
                        objectName: 'langimg'
                    }

                }
            }
            Grid
            {
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
                    text: ''
                    objectName: 'LRad'
                    id : rade
                    visible: false
                }
                Label {
                    text: ''
                    objectName: 'LRad2'
                    id : rade2
                    visible: false
                }
                GridLayout {
                    transformOrigin: Item.TopLeft
                    columns: 1
                    id : radio1grid
                    Label {
                        text: qsTr("Wert")
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
                                lCheck0.anArray[0] = text === qsTr('kombi') ? checked : false
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
                        text: qsTr("gezinkt")
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
                                rade2.text = text;
                                lCheck0.anArray[1] = text === qsTr('kombi') ? checked : false

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
            //width: listView.height
            //height: listView.height
            /*
            onVisibleChanged: {
                height = listView.height
                width = listView.height
            }*/
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
                //width: scrollView.width
                //height: scrollView.height
                /*
                onVisibleChanged: {
                    height = scrollView.height
                    width = scrollView.height
                }*/
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
                property var anObject: { "": true }
            }
            Label {
                text: "LCheck2"
                objectName: '_LCheck2_'
                id : lCheck2
                visible: false
                property var anObject: { "": true }
            }
            Label {
                text: "LCheck3"
                objectName: '_LCheck3_'
                id : lCheck3
                visible: false
                property var anObject: { "": true }
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
        Label {
            text: " "

        }
        TextField {
            objectName: "WürfFlächBenennungen"
            id : wuerfflaechNam
            text: qsTr("Wuerfelflächen Bezeichen")
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignRight
            //onSelectionStartChanged: {
            //}

            function changed() {
                augen.text = text.trim().split(/\s+/).length;
                if (text2 != text) sett=true;
                var bezeichnerlist = text.trim().split(/\s+/);
                var flag = true;
                var flag2 = true;
                var flag3 = false;
                var i = 0;
                bezeichnerlist.forEach(function(bezeichnung) {
                    if (i % 2 == 0 && !parseInt(bezeichnung, 10)) {
                    } else if ( i % 2 == 1 && parseInt(bezeichnung, 10)) {
                    } else
                        flag = false;
                    i++;
                })
                i = 0;
                if (!flag)
                    bezeichnerlist.forEach(function(bezeichnung) {
                        if (i % 3 == 0 && !parseInt(bezeichnung, 10)) {
                        } else if ( i % 3 == 1 && parseInt(bezeichnung, 10)) {
                        } else if ( i % 3 == 2 && parseInt(bezeichnung, 10)) {
                        } else
                            flag2 = false;
                        i++;
                    })

                if (bezeichnerlist.length % 2 == 0 && flag)
                    augen.text = augen.text / 2;
                else if (bezeichnerlist.length % 3 == 0 && flag2 && gewicht.position === 1)
                    augen.text = augen.text / 3;
            }
            onFocusChanged: {
                if (text === qsTr("Wuerfelflächen Bezeichen"))
                    text = "";
                changed();
            }
            onTextChanged: {
                changed();
            }
            onTextEdited: {
                changed();
            }
            property string text2: qsTr("Wuerfelflächen Bezeichen")
            property bool sett: false
        }
        Grid {
            objectName: "WürfFlächBenennungen"
            id : wuerfflaechNam2
            focus: true
            Layout.fillWidth: true
            columns: 2

            Switch {
                id: medi_
                text: qsTr("avg")
                visible : false
                objectName: "medi_"
                enabled : false
                onCheckedChanged: {
                    if (checked)
                        text = 'medi'
                    else
                        text = 'avg'
                }
            }
        }
    }

}

/*##^## Designer {
    D{i:1;anchors_x:0;anchors_y:40}
}
 ##^##*/
