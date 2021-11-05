import eel
import pyqrcode
from io import BytesIO
from base64 import b64encode

# Initialize the app
eel.init('web', allowed_extensions=['.js', '.html'])

# eel.start('index.html', size=(800, 600), mode='chrome-app')


@eel.expose
def testfunction(stringsss):
    print(stringsss)
    return stringsss


@eel.expose
def generate_qrcode(data):
    # Generate a QR code from the data
    img = pyqrcode.create(data)
    # Create a buffer to store the image
    buffer = BytesIO()
    img.png(buffer, scale=10)
    # Encode the image to base64
    return "data:image/png;base64," + b64encode(buffer.getvalue()).decode("ascii")


def main():
    # print(generate_qrcode('Hello World'))
    eel.start('index.html', size=(1200, 800))
    while True:
        eel.sleep(1)


if __name__ == '__main__':
    main()
