import cv2 as cv
import numpy as np
import HandTracking

web_cam = cv.VideoCapture(1)
web_cam.set(3, 1280)
web_cam.set(4, 720)

hand_tracking = HandTracking.HandTracking()

reset = {"up": True, "down": True}

colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]  # colours available to draw with
colour_index = 3

x_prev, y_prev = 0, 0

canvas = np.zeros((720, 1280, 3), np.uint8)

while True:

    success, img = web_cam.read()

    img = cv.flip(img, 1)  # flips image for the ease of drawing

    img = hand_tracking.find_hands(img)
    landmarks = hand_tracking.get_location(img, draw=True)

    if len(landmarks) != 0:
        x_index, y_index = landmarks[8][1:]  # index finger

        if hand_tracking.drawing() or hand_tracking.is_fist():

            if x_prev == 0 and y_prev == 0:
                x_prev, y_prev = x_index, y_index

            if hand_tracking.is_fist():  # eraser
                cv.line(img, (x_prev, y_prev), (x_index, y_index), (0, 0, 0), 100)
                cv.line(canvas, (x_prev, y_prev), (x_index, y_index), (0, 0, 0), 100)
            else:
                cv.line(img, (x_prev, y_prev), (x_index, y_index), hand_tracking.draw_colour, 15)
                cv.line(canvas, (x_prev, y_prev), (x_index, y_index), hand_tracking.draw_colour, 15)

            x_prev, y_prev = x_index, y_index

        # to change colour
        elif hand_tracking.is_thumbs_up() and reset["up"] and len(colours) != (colour_index + 1):
            colour_index += 1
            hand_tracking.draw_colour = colours[colour_index]
            reset["up"] = False

        elif hand_tracking.is_thumbs_down() and reset["down"] and colour_index != 0:
            colour_index -= 1
            hand_tracking.draw_colour = colours[colour_index]
            reset["down"] = False

        if not hand_tracking.drawing():
            x_prev, y_prev = x_index, y_index

    else:
        reset["up"] = True
        reset["down"] = True

    # puts drawing on image
    img_gray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    _, img_inverted = cv.threshold(img_gray, 50, 255, cv.THRESH_BINARY_INV)
    img_inverted = cv.cvtColor(img_inverted, cv.COLOR_GRAY2BGR)
    img = cv.bitwise_and(img, img_inverted)
    img = cv.bitwise_or(img, canvas)

    cv.imshow("AI Virtual Painter", img)
    cv.waitKey(1)
