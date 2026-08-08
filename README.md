## steganography-


A simple Python-based steganography tool for hiding and extracting text messages inside PNG images using LSB (Least Significant Bit) steganography.

# Project

- Hide text messages inside PNG images
- Extract hidden messages
- LSB-based steganography
- Simple terminal iinterface
- Automatic message capacity validation
- Lightweight and easy to use

# ProjectStructure

steganography/
├── main.py
├── steganography.py
├── requirements.txt
├── README.md
└── .gitignore

# Requirements

- Python 3.8+
- Pillow
  
# Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/steganography.git
cd steganography

# Install the dependencies:

pip install -r requirements.txt

# Usage

Run the program:

python main.py

The main menu provides three options:

[1] Hide message
[2] Extract message
[3] Exit

Hide a Message

Select:

[1] Hide message

Then provide:

Input image: input.png
Output image: secret.png
Message: Hello, this is a secret message!

The program creates a new PNG image containing the hidden message.

Extract a Message

Select:

[2] Extract message

Then provide the image containing the hidden message:

Image: secret.png

The hidden message will be displayed in the terminal.

How It Works

The project uses LSB steganography.

Each RGB pixel contains three color channels:

Red
Green
Blue

The program modifies the least significant bit of these channels to store the binary representation of the message.

For example:

Original pixel:
10110100

Modified pixel:
10110101

The visual difference is extremely small while one bit of information is stored.

Example

Original image:

input.png

After hiding:

secret.png

Extracted message:

Hello, this is my secret message!

Limitations

- PNG images are recommended.
- Large messages require larger images.
- The current version does not encrypt the message before hiding it.
- Modifying or compressing the output image can destroy the hidden data.

Disclaimer

This project is intended for educational purposes, cybersecurity laboratories, and authorized testing.

Do not use steganography to conceal information in systems or files without proper authorization.

License

This project is licensed under the MIT License.
