import cv2
import numpy as np

circle_r = 10
circle_c = (0, 0, 255)

x_pre = -1
y_pre = -1

border = 15
bgcolor = [0, 192, 192]


change_color = {
    114: (0, 0, 255),
    103: (0, 255, 0),
    98: (255, 0, 0),
    107: (0, 0, 0),
    119: (255, 255, 255)
}

OUTPUT_FILE = 'Svabbogar.png'



# inc: 1 if increase, 0 if decrease
def gte5_lte100(circle_r, inc):
    if inc:
        circle_r += 5
        return circle_r if circle_r <= 100 else 100
    else:
        circle_r -= 5
        return circle_r if circle_r >= 5 else 5




bal_eger_lenyomva = False

def mouse_event(event, x, y, flags, param):
    global bal_eger_lenyomva, circle_r, img, circle_c, x_pre, y_pre

    # bal egergomb lekezeles
    if event == cv2.EVENT_LBUTTONDOWN:
        bal_eger_lenyomva = True

    if event == cv2.EVENT_LBUTTONUP:
        bal_eger_lenyomva = False

    if event == cv2.EVENT_MOUSEMOVE:
        if bal_eger_lenyomva:
            cv2.circle(img, (x, y), circle_r, circle_c, -1)
            cv2.imshow('Pejnt', img)

    img_plus = img.copy()
    #cv2.circle(img_plus, (x_pre, y_pre), circle_r, (255, 255, 255), -1)

    cv2.circle(img_plus, (x, y), circle_r, circle_c, -1)
    cv2.imshow('Pejnt', img_plus)

    x_pre = x
    y_pre = y



# rajztabla
img = np.ndarray((480, 640, 3), np.uint8)
img.fill(255)

# rajztabla + kurzor
img_plus = np.ndarray((480, 640, 3), np.uint8)
img_plus.fill(255)

cv2.imshow('Pejnt', img)

cv2.setMouseCallback('Pejnt', mouse_event)

while True:
    key = cv2.waitKey(100)

    if key != -1:
        print(chr(key), key)

    # +
    if key == 43:
        circle_r = gte5_lte100(circle_r, 1)
        #print(circle_r)

    # -
    if key == 45:
        circle_r = gte5_lte100(circle_r, 0)
        #print(circle_r)


    # rgbkw
    if key in change_color.keys():
        circle_c = change_color[key]

    # t
    if key == 116:
        img.fill(255)
        cv2.imshow('Pejnt', img)

    # s
    if key == 115:
        cv2.imwrite(OUTPUT_FILE, img)


    if key == 113 or key == 27:
        break



cv2.destroyAllWindows()