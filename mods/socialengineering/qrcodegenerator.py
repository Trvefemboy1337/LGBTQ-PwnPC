import qrcode

def qr_code_generator():
    qr_link = input("Enter URL (make sure it starts with http:// or https://): ")
    qr_output = input("Put ur filename here: ")

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_output)
    if qr:
        print("It got saved!")
    else:
        print("It did not get saved")

