# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import cv2


html = requests.get(r'https://skillbox.ru/course/profession-python/').text
soup = BeautifulSoup(html, 'html.parser')
all_imgs = soup.find_all('img')

imgs_set = set()
for tag in all_imgs:
    url_img = tag['src']
    if url_img:
        file_name = url_img.split('/')[-1]
        file_name_full = f'all_images/{file_name}'
        if file_name_full in imgs_set:
            file_name_full = f'all_images/1{file_name}'
        imgs_set.add(file_name_full)
        with open(file_name_full, 'wb') as f:
            f.write(requests.get(url_img).content)

for imgs in imgs_set:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(imgs)
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        continue
    faces = face_cascade.detectMultiScale(
        image=gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )

    if len(faces):
        print(imgs)
