import base64
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify
from waitress import serve
from threading import Lock

app = Flask(__name__)
thread_lock = Lock()
model = tf.keras.models.load_model("generator.h5")

def generate_image():
    inp = tf.random.normal((1, 100))
    res = model.predict(inp)
    res = ((res[0]+1)*127.5).astype(np.uint8)
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

@app.route("/", methods=["GET"])
def root():
    return jsonify("OK")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
