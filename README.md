# QR Code Generator

This repository contains a simple Python script for generating QR codes. It allows users to encode text-based data, such as URLs, contact information, Wi-Fi credentials, and more, into QR codes that can be scanned with smartphones or QR code readers.

## Features

Generate QR codes for any text input.

Save the QR code as an image file (e.g., PNG).

Customize the QR code's appearance (e.g., colors).

## Requirements

Python 3.6 or higher

qrcode library (with Pillow for image generation)

## Installation

Step 1: Clone the Repository

git clone <repository_url>
cd <repository_directory>

Step 2: Set Up the Environment

Option 1: Using a Virtual Environment (Recommended)

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

Install the required library:

pip install qrcode[pil]

Option 2: Install Globally (Use Caution)

Run the following command:

pip install qrcode[pil] --break-system-packages

## Basic Usage

Run the script:

'''python qr_generator.py
'''

Follow the prompts:

Enter the data you want to encode (e.g., a URL, text, or contact information).

Specify the output file name (e.g., qrcode.png).

The QR code will be saved in the current directory.

For URLs

Provide a URL (e.g., https://www.example.com) as the input data.

Save the output file (e.g., example_qr.png).

For Contact Information (vCard/MeCard)

Input data can be formatted as vCard or MeCard text to encode contact details.
Example:

BEGIN:VCARD
VERSION:3.0
N:Doe;John;;;
FN:John Doe
ORG:Example Company
TITLE:Software Engineer
TEL:+1234567890
EMAIL:john.doe@example.com
END:VCARD

For Wi-Fi Sharing

Input the Wi-Fi credentials in the following format:

WIFI:S:YourWiFiName;T:WPA;P:YourPassword;;

Save the QR code for sharing.

For Custom Colors

Modify the script to customize colors:

img = qr.make_image(fill_color="blue", back_color="yellow")

Example Input and Output

Input:

Enter the data to encode in the QR code: https://www.example.com
Enter the output filename (e.g., 'qrcode.png'): example_qr.png

Output:

A QR code image saved as example_qr.png.


## Customization

The script can be modified to change the appearance of the QR codes, such as colors or embedded logos. To change the colors, update the following section in the script:

img = qr.make_image(fill_color="blue", back_color="yellow")

## Applications

Sharing website links

Storing contact information (vCard/MeCard)

Wi-Fi network sharing

Payment systems (e.g., PayPal, Bitcoin)

Event information

Location sharing

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request.