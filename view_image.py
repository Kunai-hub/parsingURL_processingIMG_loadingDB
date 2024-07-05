# -+- coding: utf-8 -*-

import cv2


def view_image(image, name_of_window):
    """
    Вывод картинки в окно

    :param image: картинка
    :param name_of_window: имя окна
    :return: None
    """
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
