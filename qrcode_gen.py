import qrcode

def generate_qr_code(data, output_file):
    """
    Generate a QR code with the given data and save it to a file.
    
    Args:
        data (str): The data to encode in the QR code.
        output_file (str): The filename for the saved QR code image (e.g., 'qrcode.png').
    """
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border thickness (minimum is 4)
    )
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR Code image
    img.save(output_file)
    print(f"QR code generated and saved as {output_file}")


if __name__ == "__main__":
    # Input data for the QR code
    data_to_encode = input("Enter the data to encode in the QR code: ")
    output_filename = input("Enter the output filename (e.g., 'qrcode.png'): ")

    # Generate the QR code
    generate_qr_code(data_to_encode, output_filename)
