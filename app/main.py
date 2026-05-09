from flask import Flask, Response
from PIL import Image, ImageDraw
from io import BytesIO
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>k3s Python Image Demo</h1>
    <p>Try <a href="/image">/image</a></p>
    """


@app.route("/image")
def image():
    img = Image.new("RGB", (600, 300), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)

    draw.text((40, 60), "Hello from Python on k3s!", fill=(0, 0, 0))
    draw.text(
        (40, 110), f"Generated at: {datetime.utcnow().isoformat()} UTC", fill=(0, 0, 0)
    )
    draw.text((40, 160), "Deployed via GitHub Actions", fill=(0, 0, 0))

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
