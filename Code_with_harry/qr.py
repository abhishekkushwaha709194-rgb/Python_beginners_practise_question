import qrcode

# =========================
# CUSTOM SETTINGS
# =========================

data = "Aadarsh gandu"

output_file = "my_qr.png"

# QR colors
fill_color = "white"
background_color = "black"

# QR size
box_size = 10
border = 4

# =========================
# CREATE QR CODE
# =========================

qr = qrcode.QRCode(
    version=None,  # Automatically choose QR size
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=box_size,
    border=border
)

qr.add_data(data)
qr.make(fit=True)

# Generate image
img = qr.make_image(
    fill_color=fill_color,
    back_color=background_color
)

# Save
img.save(output_file)

print(f"QR code saved as: {output_file}")