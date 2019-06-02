#!/usr/bin/env python3
from PIL import Image
import argparse
import sys

parser = argparse.ArgumentParser(description="Become a poly sci major with one CLI")
parser.add_argument("-s", type = float, help = "scale at which icons should appear w.r.t. width", default = 0.1)
parser.add_argument("-b", type = str, help = "background image", default = "compass.png")
args = parser.parse_args()
image_scale = args.s
bg = args.b


def place(bg, lang, econ, auth):
	wd, ht = bg.size
	lang_img = Image.open(lang)
	lang_img.thumbnail((int(image_scale*wd), int(image_scale*wd)), Image.ANTIALIAS)
	bg.paste(lang_img, (int(wd*econ), int(ht*(1-auth))), lang_img)

background = Image.open(args.b)
for lang in sys.stdin:
	econ, auth, name = lang.split(' ')
	place(background, name.strip(), float(econ), float(auth))
background.show()
