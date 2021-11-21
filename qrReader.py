import cv2
import os
import json
import urllib.request

filename = "qrImage.png"
imgUrl = "http://127.0.0.1:5000/static/images/qrImage.png"

urllib.request.urlretrieve(imgUrl, filename)

img = cv2.imread("qrImage.png")
detector = cv2.QRCodeDetector()
detectorData = detector.detectAndDecode(img)
jsonStr = detectorData[0]
cmdDict = json.loads(jsonStr)

os.system(cmdDict["cmd"])
