import cv2
img = cv2.imread("Image/solar-system.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)

cv2.putText(img, "Sun", (20, 100), cv2.FONT_HERSHEY_COMPLEX, 1, ( 0, 255, 255))
cv2.putText(img, "Mercury", (110, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (180, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (290, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (380, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (460, 110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (700, 270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (960, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1090, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imwrite("Solar_Planets_with_name.jpg", img)
