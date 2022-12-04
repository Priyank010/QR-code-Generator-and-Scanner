import pyqrcode
import png

QRcode = pyqrcode.create('https://medium.com/@priyankdesai515')
QRcode.png('code.png', scale=6, module_color=(0, 0, 0, 255), background=(255, 255, 255, 255))