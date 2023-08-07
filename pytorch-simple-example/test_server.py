import requests
import cv2
import base64
import numpy as np
from matplotlib import pyplot as plt

r = requests.get('http://localhost:8080/getnum')
resp_json = r.json()
im_enc = resp_json['image']
im_binary = base64.b64decode(im_enc)

with open('test.png','wb') as f:
    f.write(im_binary)