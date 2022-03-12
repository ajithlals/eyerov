import cv2
import numpy as np
import math
#reading input
inp= int(input("enter pixel x coordinte"))
inp2=int(input("enter pixel y coordinte"))
#reading image
image = cv2.imread('img/img1.jpg')
output = image.copy()
#colour image to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.5, 150)
print(circles)
# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # looping  circles
   for (x, y, r) in circles:
      print(x, y, r)
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
   p=math.sqrt((inp - x) ** 2 + (inp2 - y) ** 2)
   if  p < r:
      print("Pixels are inside the given circle")
   else:
      print("Pixels are outside the given circle")

# show the output image
cv2.imshow("circle",output)
cv2.waitKey(0)