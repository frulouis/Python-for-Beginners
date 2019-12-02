# -*- coding: utf-8 -*-
# @Time    : 2019/12/01 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : API_Operations.py
# @Software: PyCharm
# @Comments:


# ======================================================================================
# Table Of Content
# Concept 8.1.0: How to use an API with Python 
# ======================================================================================


# ======================================================================================
# Concept 8.1.0: How to use an API with Python 
# ======================================================================================

# >>>>
# Source Code Link: https://rapidapi.com/blog/how-to-use-an-api-with-python/
# Acccessed: 12/01/2019

import re

import imageio
import requests
from skimage import transform, io

# get json with information (including name and date) about Earth pictures
response = requests.post("https://NasaAPIdimasV1.p.rapidapi.com/getEPICEarthImagery",
                         headers={
                             "X-RapidAPI-Host": "NasaAPIdimasV1.p.rapidapi.com",
                             "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                             "Content-Type": "application/x-www-form-urlencoded"
                         }
                         )
# convert json to Python object 
data = response.json()
# create regex pattern to get separately year, month and day of an image
dates_pattern = r"^(?P<year>d{4})-(?P<month>d{2})-(?P<day>d{2})"
# download images and save each to ./images folder
for img in data['contextWrites']['to']:
    # get year, month and day with regex to create image url
    matches = re.search(dates_pattern, img['date'])
    year = matches.group('year')
    month = matches.group('month')
    day = matches.group('day')
    image_name = img['image']
    img_url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
    # save image to ./images folder
    img_data = requests.get(img_url).content
    with open(f'images/{image_name}.png', 'wb') as handler:
        handler.write(img_data)
index = range(len(data['contextWrites']['to']))
images = []
# resize images and create gif from them
for i in index:
    img_name = data["contextWrites"]["to"][i]["image"]
    img = io.imread(f'images/{img_name}.png')
    small_img = transform.resize(img, (500, 500), mode='symmetric', preserve_range=True)
    images.append(small_img)
imageio.mimsave('images/earth500.gif', images)
