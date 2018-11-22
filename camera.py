#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:35:11 2018

@author: OmarDiboCalixtoAfrangeNeto
"""

import cv2 
     
class Camera:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        self.captura = cv2.VideoCapture(0) 
        
    def Webcam(self):
        ret, img = self.captura.read()  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5) 
        if len(faces)>0:
            estado='Aceso'
        else:
            estado='Apagado'
        
        k = cv2.waitKey(1)
        self.after(200, self.Webcam)
