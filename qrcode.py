import qrcode

img = qrcode.make("https://www.youtube.com/@VihimGamz")
img.save("channel.jpg")

img = qrcode.make("hello brother how are you")
img.save("greeting.jpg")
