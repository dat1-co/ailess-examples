import base64
import cv2
import numpy as np
import torch
from flask import Flask, jsonify
from waitress import serve
from threading import Lock
from models import Generator, nz

app = Flask(__name__)
thread_lock = Lock()

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")
model = Generator()
model.load_state_dict(torch.load('generator.pth', map_location='cpu'))
model.to(device).eval()

def generate_image():
    with torch.no_grad():
        inp = torch.randn(1, nz, 1, 1).to(device)
        res = model(inp)
        res = res.cpu().numpy()
        res = ((res[0, 0]+1)*127.5).astype(np.uint8)
        return res

def img_2_b64(img):
    img_enc = cv2.imencode(".png", img)[1]
    return base64.b64encode(img_enc.tobytes()).decode("utf-8")

@app.route("/getnum", methods=["GET"])
def getnum():
    with thread_lock:
        image = generate_image()
        image = img_2_b64(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        print("Image generated")
        return jsonify({"image": image})

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)