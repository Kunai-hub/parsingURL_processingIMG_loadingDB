# -*- coding: utf-8 -*-

import cv2


def draw_mustache(img, x, y, w, h):
    """
    Рисование "усов" на картинке, если там выявлено лицо.

    :param img: картинка
    :param x: точка начала по x
    :param y: точка начала по y
    :param w: точка конца по x
    :param h: точка конца по y
    :return: None
    """
    mw = w * 2 // 5
    mh = h // 10
    mx = x + w // 2 - mw // 2
    my = y + h * 2 // 3
    # cv2.rectangle(img, (mx, my), (mx+mw, my+mh), (0, 0, 0), 1)
    hair_w = max(mw // 20, 1)
    for dx in range(mw // hair_w):
        cv2.line(img, (mx + hair_w * dx, my), (mx + hair_w * (dx + 1), my + mh), (0, 0, 0), 1)
        cv2.line(img, (mx + hair_w * dx, my + mh), (mx + hair_w * (dx + 1), my), (0, 0, 0), 1)
