# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import cv2
from draw_mustache import draw_mustache
from view_image import view_image
import database_creating


html = requests.get(r'https://skillbox.ru/course/profession-python/').text
soup = BeautifulSoup(html, 'html.parser')
all_images = soup.find_all('img')

images_set = set()
for tag in all_images:
    url_img = tag['src']
    if url_img:
        file_name = url_img.split('/')[-1]
        file_name_full = f'all_images/{file_name}'
        if file_name_full in images_set:
            file_name_full = f'all_images/1{file_name}'
        images_set.add(file_name_full)
        with open(file_name_full, 'wb') as f:
            f.write(requests.get(url_img).content)

for images in images_set:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(images)
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
        # print(images)
        for (x, y, w, h) in faces:
            draw_mustache(img, x, y, w, h)
        # view_image(img, images)
        images_with_mustache = images.replace('all_images', 'results_images')

        cv2.imwrite(images_with_mustache, img)

        database_creating.Mustache.create_table()
        database_creating.Mustache.create(name=images_with_mustache)

print(list(database_creating.Mustache.select()))
