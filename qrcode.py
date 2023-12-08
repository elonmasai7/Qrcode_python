#pip install qrcode
import qrcode

data ="https://masaielon.netlify.app"
img = qrcode.make(data)


img.save ("qrcode.png")