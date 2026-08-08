from PIL import Image


END_MARKER = "<<<END>>>"


def hide_message(input_image, output_image, message):
    """Hide a text message inside a PNG image."""

    image = Image.open(input_image).convert("RGB")

    binary_message = "".join(format(ord(char), "08b") for char in message + END_MARKER)

    pixels = list(image.getdata())

    if len(binary_message) > len(pixels) * 3:
        raise ValueError("The message is too large for this image.")

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel
        channels = [r, g, b]

        for i in range(3):
            if bit_index < len(binary_message):
                channels[i] = (channels[i] & ~1) | int(binary_message[bit_index])
                bit_index += 1

        new_pixels.append(tuple(channels))

    image.putdata(new_pixels)
    image.save(output_image, "PNG")


def extract_message(input_image):
    """Extract a hidden text message from a PNG image."""

    image = Image.open(input_image).convert("RGB")
    pixels = list(image.getdata())

    binary_message = ""

    for pixel in pixels:
        for channel in pixel:
            binary_message += str(channel & 1)

    chars = []

    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]

        if len(byte) < 8:
            break

        char = chr(int(byte, 2))
        chars.append(char)

        message = "".join(chars)

        if message.endswith(END_MARKER):
            return message[:-len(END_MARKER)]

    raise ValueError("No hidden message was found.")
