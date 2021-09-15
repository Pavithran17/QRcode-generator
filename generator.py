import qrcode
import matplotlib.pyplot as plt
data="https://github.com/Pavithran17/QRcode-generator/new/main"
filename="myqrcode.png"
image=qrcode.make(data)
image.save(filename)
plt.imshow(image,cmap='gray')
