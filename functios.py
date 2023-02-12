import math

import cv2 as cv
import numpy as np

# Contours w/ greatest number of points
# TODO max by area

def max_contour(contours):
    max_val = 0
    max_cnt = None
    for contour in contours:
        if cv.contourArea(contour) > max_val:
            max_cnt = contour
            max_val = cv.contourArea(contour)

    return max_cnt


def create_cones_contours():
    """
    TODO: Add so it works with straight or tipped cone (with a parameter of a folder path)
    :return:
    """

    lower = np.array([14, 100, 65])
    higher = np.array([35, 255, 255])
    cones = []
    for i in range(1, 25):
        path = "C:\\Users\\itayo\\Charged_Up_2023_Vision\\cones\\cone" + str(i) + ".jpg"
        cone = cv.imread(path)

        hsv = cv.cvtColor(cone, cv.COLOR_BGR2HSV)
        h, w = cone.shape[:2]
        mask = cv.inRange(hsv, lower, higher);
        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Only get the biggest one
        cnt = max_contour(contours)

        cones.append(cnt)

    return cones


def cone_shape_match(contour, cones_contours):
    """

    :param contour:
    :param cones_contours:
    :return: The match number of the given contour and straight standing cone
    """

    for cnt in cones_contours:
        ret = cv.matchShapes(contour, cnt, 1, 0.0)
        if ret < 0.2:
            print("matchhh: ", ret)
            return True

    # cv.drawContours(cone1, bc, -1, (0, 255, 0), 3)
    # cv.imshow('hsv', hsv)
    # cv.imshow('mask', mask)

    return False


def get_cone_angle(frame, contour):
    """

    :param frame: The frame to find angle in
    :param contour: The contour to calculate its angle
    :return: The angle between the cone and the camera horizontal axis
    """

    rows, cols = frame.shape[:2]
    [vx, vy, x, y] = cv.fitLine(contour, cv.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    #cv.line(frame, (cols - 1, righty), (0, lefty), (255, 0, 0), 2)

    m = (lefty - righty) / ((cols-1) - 0)
    angle = math.degrees(math.atan(m - 0))
    return angle
