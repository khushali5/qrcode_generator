import os
import qrcode

def generate_qr_code(data, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the generated QR code to the output folder
    output_path = os.path.join(output_folder, "output_qr_code.png")
    img.save(output_path)

    print(f"QR Code generated and saved at: {output_path}")

if __name__ == "__main__":
    # Data to be encoded in the QR code
    data_to_encode = "LNCT150"

    # Output folder for saving the generated QR code
    qr_output_folder = "generated_qr_codes"

    # Generate QR code
    generate_qr_code(data_to_encode, qr_output_folder)


