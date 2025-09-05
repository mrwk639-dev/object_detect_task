import cv2
import numpy as np
image = cv2.imread("test.jpg")
final_im=image.copy()

image=cv2.GaussianBlur(image, (5,5), 0)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.Canny(image, 100, 200)
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    cv2.drawContours(final_im, [approx], -1, (0, 255, 0), 3)


    mask = np.zeros(final_im.shape[0:2], dtype=np.uint8)
    cv2.drawContours(mask, [approx], -1, 255, -1)
    b, g, r = cv2.mean(final_im, mask=mask)[:3]
    b, g, r = int(b), int(g), int(r)
    hsv=cv2.cvtColor(np.uint8([[[b,g,r]]]), cv2.COLOR_BGR2HSV)[0][0]
    h,s,v=hsv


    color = "Undefine"
    if h<= 10 or h>= 160:
        color = "Red"
    elif 35 < h <= 85:
        color = "Green"
    elif 100 < h <= 130:
        color = "Blue"

    shape = "Undefine"
    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"
    elif len(approx) >=5:
        shape = "Circle"

    

    cv2.putText(final_im, shape, (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.putText(final_im, color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    


cv2.imshow("image", final_im)
cv2.waitKey(0)
cv2.destroyAllWindows()