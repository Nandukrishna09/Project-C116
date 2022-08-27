import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (240,248,255)
            )

cv2.putText(img,
            "Mercury",
            (120,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (240,248,255))

cv2.putText(img,
            "Venus",
            (200,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (240,248,255))

cv2.putText(img,
            "Earth",
            (280,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (240,248,255))

cv2.putText(img,
            "Mars",
            (385,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (240,240,240))

cv2.putText(img,
            "Jupiter",
            (500,250),
            cv2.FONT_HERSHEY_COMPLEX,
            1.2,
            (1,1,1))

cv2.putText(img,
            "Saturn",
            (750,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (950,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (1,1,1))

cv2.putText(img,
            "Neptune",
            (1100,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (1,1,1))

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)