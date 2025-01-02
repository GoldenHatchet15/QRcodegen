from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


def generate_qr_code(data):
    """
    Generate a QR code as an in-memory image file.
    Args:
        data (str): Data to encode in the QR code.
    Returns:
        BytesIO: A file-like object containing the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data")
        if not data:
            return render_template("index.html", error="Please enter some data to encode.")
        qr_code_img = generate_qr_code(data)
        return send_file(qr_code_img, mimetype="image/png", as_attachment=True, download_name="qrcode.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
