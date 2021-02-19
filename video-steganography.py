import cv2
import numpy as np
import zipfile
import sys
import os
import datetime

dirname = "file-{}".format(datetime.today());
os.mkdir(dirname)
os.chdir(dirname)


filepath = ''

if(len(sys.argv) == 1):
	filepath = input("Enter the filepath of file to extract: ")
else:
	filepath = sys.argv[1]

with zipfile.ZipFile(filepath) as zObj:
	zObj.extractall(os.getcwd())

def find(arr,item):
	for i in range(len(arr)):
		if arr[i] == item:
			return i
	return None

def getFile():
	files = os.listdir()
	extensions = [ files[i].split('.')[1]  for i in range(len(files)) ]
	return (files[find(extensions,'txt')],files[find(extensions,'mp4')])


def captureVideoAndHide():
	f = open(getFile()[0],'r')
	cap = cv2.VideoCapture(getSecretText()[1])
	while(cap.isOpened()):
		ret,frame = cap.read()
			
