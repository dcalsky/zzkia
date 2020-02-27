import base64
import io
import os
from typing import Tuple
from collections import deque
from PIL import Image, ImageFont, ImageDraw, ImageOps

font_size = 70
line_gap = 20
body_pos = (200, 330)
subtitle_pos = (790, 320)
body_color = (0, 0, 0, 255)
subtitle_color = (129, 212, 250, 255)
line_rotate = -9.8
max_line_width = 680
max_content_height = 450
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


def generate_image(text: str):
    origin_im = Image.open("images/3.png")
    text = text[:900]
    length = len(text)
    width, height = font.getsize(text)
    current_width = 0
    lines = []
    line = ""
    q = deque(text)

    while q:
        word = q.popleft()
        width, _ = font.getsize(word)
        current_width += width
        if current_width >= max_line_width:
            q.appendleft(word)
            lines.append(line)
            current_width = 0
            line = ""
        else:
            line += word
    lines.append(line)
    image2 = Image.new("RGBA", (max_line_width, max_content_height))
    draw2 = ImageDraw.Draw(image2)
    for i, line in enumerate(lines):
        y = i * (height + line_gap)
        if y > max_content_height: break
        draw2.text((0, y), text=line, font=font, fill=body_color)
    image2 = image2.rotate(line_rotate, expand=1)

    px, py = body_pos
    sx, sy = image2.size
    origin_im.paste(image2, (px, py, px + sx, py + sy), image2)
    draw_subtitle(origin_im, f"{length}/900")
    # origin_im.save("results/final.png", "png") Save as local file
    return im_2_b64(origin_im)

