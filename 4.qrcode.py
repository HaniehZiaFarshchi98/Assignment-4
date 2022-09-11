import qrcode
text = input ("please enter your text:")
address = input ("please enter your address:")
Qrcode = qrcode.make( text , address)
Qrcode.save("qrcode.jpg")