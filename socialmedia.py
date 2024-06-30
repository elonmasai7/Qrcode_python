import qrcode

social_media_links = {
    "LinkedIn": "https://www.linkedin.com/in/elonmasai/",
    "Twitter": "https://twitter.com/elonmasai7",
    "Instagram": "https://www.instagram.com/macgraffixkenya/",
    "GitHub": "https://github.com/elonmasai7",
    "Facebook": "https://www.facebook.com/elonmasai"
}

all_links = "\n".join([f"{platform}: {url}" for platform, url in social_media_links.items()])

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(all_links)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("social_media_qr.png")

print("QR code generated and saved as 'social_media_qr.png'")
