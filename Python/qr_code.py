import qrcode

print("="*46)
print("   Bienvenue sur le générateur de QR Code : ")
print("="*46)

url = input("Entrez l'URL : ").strip()
file_path = "C:\\Users\\user\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("✅ Le QR Code a été généré ! ✅")

