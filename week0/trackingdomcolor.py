# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:10:03 2020

@author: zefyr
Code adapted from:
https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
This version retains original colorspace, takes video instead of input image,
restricts processing to a small rectangle in the middle of the video indicated
by bounding box, and displays both video and constantly updating histogram
with dominant color indicated.
"""

import cv2
import numpy as np
from sklearn.cluster import KMeans

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

cap = cv2.VideoCapture(0)

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    m = max(hist)
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        if percent == m:
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      (0,255,0),2)
        startX = endX

    # return the bar chart
    return bar

while(1):

    # Take each frame
    _, frame = cap.read()

    img = frame[220:260, 290:350, :]
    
    img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(img)
    
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)
    cv2.imshow('res',bar)
    cv2.imshow('frame',cv2.rectangle(frame,(290, 220), (350,260), (0,255,0),2))
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()