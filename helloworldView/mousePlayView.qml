import QtQuick 1.1

Rectangle {
    width: 200
    height: 200
    color: "white"

    Text {
        anchors.centerIn: parent
        text: "Hello World"
        color: "black"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("Mouse clicked!", parent.color)

                if(parent.color == "#000000")
                    parent.color = "blue"
                else
                    parent.color = "black"
            }
        }
    }
}
