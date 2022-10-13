import imp


import pyqrcode

from pyqrcode import QRCode

link = "https://praiz.tech.blog/"

img = pyqrcode.create(link)
img.svg("qrcode.svg", scale = 8)