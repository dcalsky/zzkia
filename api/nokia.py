import textwrap
import base64
import io
import os
from typing import Tuple
from PIL import Image, ImageFont, ImageDraw, ImageOps

font_size = 70
line_gap = 20
line_width = 9
body_pos = (260, 340)
subtitle_pos = (790, 320)
body_color = (0, 0, 0, 255)
subtitle_color = (129, 212, 250, 255)
line_rotate = -9.1
font = ImageFont.truetype("fonts/1.ttf", font_size)


def image_to_byte_array(image: Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def im_2_b64(image):
    buff = io.BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str


def draw_subtitle(im, text: str):

    width, height = font.getsize(text)
    image2 = Image.new("RGBA", (width, height))
    draw2 = ImageDraw.Draw(image2)
    draw2.text((0, 0), text=text, font=font, fill=subtitle_color)
    image2 = image2.rotate(line_rotate, expand=1)

    px, py = subtitle_pos
    sx, sy = image2.size
    im.paste(image2, (px, py, px + sx, py + sy), image2)


def generate_image(text: str, path=None):
    im = Image.open(path or "images/3.png")
    length = len(text)
    width, height = font.getsize(text)
    lines = textwrap.wrap(text, width=line_width)
    image2 = Image.new("RGBA", (width, (height + line_gap) * len(lines)))
    draw2 = ImageDraw.Draw(image2)
    for i, line in enumerate(lines):
        draw2.text((0, i * (height + line_gap)), text=line, font=font, fill=body_color)
    image2 = image2.rotate(line_rotate, expand=1)

    px, py = body_pos
    sx, sy = image2.size
    im.paste(image2, (px, py, px + sx, py + sy), image2)
    draw_subtitle(im, f"{length}/900")
    # im.save("results/final.png", "png")
    return im_2_b64(im)

