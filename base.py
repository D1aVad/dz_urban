import cv2
import numpy as np

mtx = cv2.imread('image/color_text.jpg')

new = np.zeros(mtx.shape, dtype='uint8')

#kernel = np.ones((5, 5), np.uint8)

mtx = cv2.cvtColor(mtx, cv2.COLOR_BGR2GRAY)
mtx = cv2.Canny(mtx, 30, 30)
#mtx = cv2.dilate(mtx, kernel, iterations=1)
#mtx = cv2.erode(mtx, kernel, iterations=1)


con, hir = cv2.findContours(mtx, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#cv2.drawContours(new, con, -1, (0, 0, 255), 1)
for contour in con:
    # Проверка, находится ли контур в нужных координатах
    x, y, w, h = cv2.boundingRect(contour)
    if x >= 0 and x <= 700 and y >= 0 and y <= 140:
        # Рисование выбранных контуров на черном фоне
        cv2.drawContours(new, [contour], -1, (0, 255, 0), 2)  # Зеленый цвет и толщина 2 пикселя
for contour in con:
    # Проверка, находится ли контур в нужных координатах
    x, y, w, h = cv2.boundingRect(contour)
    if x >= 0 and x <= 800 and y >= 158 and y <= 300:
        # Рисование выбранных контуров на черном фоне
        cv2.drawContours(new, [contour], -1, (0, 0, 255), 2)  # Зеленый цвет и толщина 2 пикселя
for contour in con:
    # Проверка, находится ли контур в нужных координатах
    x, y, w, h = cv2.boundingRect(contour)
    if x >= 0 and x <= 700 and y >= 300 and y <= 700:
        # Рисование выбранных контуров на черном фоне
        cv2.drawContours(new, [contour], -1, (255, 0, 255), 2)  # Зеленый цвет и толщина 2 пикселя
cv2.imshow('Result', new)
cv2.waitKey(0)