const show_message = document.getElementById("content");
const web_socket = new WebSocket("ws://localhost:8080/chat");



function send_message() {
    const input_message = document.getElementById("msg");
    const message = input_message.value;
    if (message !== null) {
        console.log(message.length);
        web_socket.send(message);
        input_message.value = "";
    }
}

web_socket.onmessage = function (event) {
    let new_node = document.createElement("p");
    new_node.innerText = event.data;
    show_message.appendChild(new_node);
};