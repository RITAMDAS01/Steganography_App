from PIL import Image

# Encrypt the image with message + password + end marker
def encrypt_image(image_path, message, password, output_path):
    img = Image.open(image_path).convert("RGB")
    encoded = img.copy()
    width, height = img.size

    # Add end marker to detect the end of the message during decryption
    secret = password + message + "#####"
    binary_secret = ''.join(format(ord(i), '08b') for i in secret)

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_secret):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(binary_secret[data_index])
                encoded.putpixel((x, y), (r, g, b))
                data_index += 1
    encoded.save(output_path)


# Decrypt the image and stop at the end marker
def decrypt_image(image_path, password):
    img = Image.open(image_path).convert("RGB")
    binary_data = ''

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''.join(chr(int(byte, 2)) for byte in all_bytes)

    if not decoded.startswith(password):
        return "Invalid password!"
    
    decoded_message = decoded[len(password):]
    end_marker_index = decoded_message.find("#####")
    
    if end_marker_index == -1:
        return "End marker not found! Message may be corrupted."
    
    return decoded_message[:end_marker_index]
