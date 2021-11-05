function generate_qrcode() {
    // Get the value from the input field
    var data = document.getElementById("data").value;
    eel.generate_qrcode(data)(generate_image);
}

function generate_image(base64) {
    document.getElementById("qr").src = base64;
}