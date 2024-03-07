import cv2 as cv
import mediapipe as mp


class HandTracking():
    def __init__(self):

        self.draw_colour = (255, 0, 255)
        self.finger_tips = [4, 8, 12, 16, 20]

        self.mpDraw = mp.solutions.drawing_utils
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(0.85)

    def find_hands(self, img, draw=True):

        img_rgb = cv.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(img_rgb)

        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

        return img

    def get_location(self, img, hand_number=0, draw=True):

        self.landmarks = []

        if self.result.multi_hand_landmarks:

            hand = self.result.multi_hand_landmarks[hand_number]

            for hand_id, landmark in enumerate(hand.landmark):

                h, w, c = img.shape
                x, y = int(landmark.x * w), int(landmark.y * h)

                self.landmarks.append([hand_id, x, y])

                if hand_id == 8 and draw:  # draws the coloured circle at the tip of the index finger
                    cv.circle(img, (x, y), 20, self.draw_colour, cv.FILLED)

        return self.landmarks

    def how_many_fingers_up(self):

        fingers_up = []

        if self.landmarks[self.finger_tips[0]][1] < self.landmarks[self.finger_tips[0] - 1][1]:
            fingers_up.append(1)
        else:
            fingers_up.append(0)

        for hand_id in range(1, 5):
            if self.landmarks[self.finger_tips[hand_id]][2] < self.landmarks[self.finger_tips[hand_id] - 2][2]:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

        return fingers_up

    def is_thumbs_up(self):

        # 1 is x, horizontal
        # 2 is y, vertical
        if self.landmarks[self.finger_tips[0]][2] >= self.landmarks[self.finger_tips[0] - 1][2]:
            return False

        for hand_id in range(1, 5):
            if self.landmarks[self.finger_tips[hand_id]][2] <= self.landmarks[self.finger_tips[0]][2]:
                return False

        if len(self.landmarks) < 21:
            return False

        if self.landmarks[6][2] - self.landmarks[self.finger_tips[0]][2] < 30:
            return False

        return True

    def is_thumbs_down(self):

        # 1 is x, horizontal
        # 2 is y, vertical
        if self.landmarks[self.finger_tips[0]][2] <= self.landmarks[self.finger_tips[0] - 1][2]:
            return False

        for hand_id in range(1, 5):
            if self.landmarks[self.finger_tips[hand_id]][2] >= self.landmarks[self.finger_tips[0]][2]:
                return False

        if len(self.landmarks) < 21:
            return False

        if self.landmarks[6][2] - self.landmarks[self.finger_tips[0]][2] > -30:
            return False

        return True

    def is_fist(self):

        fingers = self.how_many_fingers_up()

        if (not fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]
                and not self.is_thumbs_up() and not self.is_thumbs_down() and not self.drawing() and not self.selection()):
            return True

        return False

    def drawing(self):

        fingers = self.how_many_fingers_up()

        if (fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]
                and not self.is_thumbs_up() and not self.is_thumbs_down()):  # drawing mode
            return True

        return False

    def selection(self):

        fingers = self.how_many_fingers_up()

        if (fingers[1] and fingers[2]
                and not self.is_thumbs_up() and not self.is_thumbs_down()):  # selecting colour mode
            return True

        return False


# to try out only hand tracking
if __name__ == '__main__':
    web_cam = cv.VideoCapture(1)

    hand_tracking = HandTracking()

    while True:
        success, img = web_cam.read()

        img = hand_tracking.find_hands(img, draw=True)

        cv.imshow("Image", img)
        cv.waitKey(1)
