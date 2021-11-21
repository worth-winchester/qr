import cv2
import os
import json

img = cv2.imread("static/images/qrImage.png")
detector = cv2.QRCodeDetector()
detectorData = detector.detectAndDecode(img)
jsonStr = detectorData[0]
cmdDict = json.loads(jsonStr)

os.system(cmdDict["cmd"])

#for each in cmdDict["cmdList"]:
#    os.system(each)
