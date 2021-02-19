import os
import qrcode
from PIL import Image
from hello import test


# Problem1
print(os.getcwd())

# Problem2
test()

# Problem3
img = Image.open("起风了.jpg")
img.show()

# Problem4
img_qrcode = qrcode.make(r"https:\\bilibili.com")
img_qrcode.show()
