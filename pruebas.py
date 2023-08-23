llave = 22
with open("image-removebg-preview.png", mode="rb") as image:
    image_content = image.read()
    image_content = bytearray(image_content)
    for index, value in enumerate(image_content):
        image_content[index] = value ^ llave
with open("image-removebg-preview-encr.png", mode="wb") as new_image:
    new_image.write(image_content)
print("Encryption done")
#Decrypt
with open("image-removebg-preview-encr.png", mode="rb") as image_2:
    image_2_content = image_2.read()
    image_2_content = bytearray(image_2_content)
    for index, value in enumerate(image_2_content):
        image_2_content[index] = value ^ llave
with open("image-removebg-preview-encr-decr.png", mode="wb") as new_image_2:
    new_image_2.write(image_2_content)
print("Decryption")
