import cv2
import numpy as np
import math
inp= int(input("enter pixel coordintes"))
inp2=int(input("enter pixel coordintes"))
image = cv2.imread('img1.jpg')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 180,param1= 50, param2=30, minRadius= 5,maxRadius=100)
print(circles)
# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # loop over the circles
   for (x, y, r) in circles:
      print(x, y, r)
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
   p=math.sqrt((inp - x) ** 2 + (inp2 - y) ** 2)
   if  p < r:
      print("inside")
   else:
      print("outside")

# show the output image
cv2.imshow("circle",output)
cv2.waitKey(0)