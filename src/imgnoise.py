# Img noise
# A python script to add noise to images.
# Github: https://www.github.com/aweomelewis2007/img_noise
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import PIL
from PIL import Image
import random

def brightness(file, output):
    image = Image.open(file)
    image = image.convert("RGB")
    width, height = image.size
    brightened_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            brightness_value = random.randint(-100, 100)
            new_r = max(0, min(255, r + brightness_value))
            new_g = max(0, min(255, g + brightness_value))
            new_b = max(0, min(255, b + brightness_value))
            brightened_image.putpixel((x, y), (new_r, new_g, new_b))
    brightened_image.save(output)

def colour(file, output):
    image = Image.open(file)
    image = image.convert("RGB")
    width, height = image.size
    coloured_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r_shift = random.randint(-100, 100)
            g_shift = random.randint(-100, 100)
            b_shift = random.randint(-100, 100)
            new_r = max(0, min(255, r + r_shift))
            new_g = max(0, min(255, g + g_shift))
            new_b = max(0, min(255, b + b_shift))
            coloured_image.putpixel((x, y), (new_r, new_g, new_b))
    coloured_image.save(output)