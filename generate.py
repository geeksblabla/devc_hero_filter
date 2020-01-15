from PIL import Image # install the PIL module, better use the well maintained Pillow fork // pip install pillow
background = Image.open("devc_hero_img.jpg") #  profile image from fb
foreground = Image.open("devc_hero_band.png") # the devc hero band png image
size = 588, 588
background.thumbnail(size)
backgroundGey = background.convert(mode="L", matrix=None, dither=None, palette=0, colors=0)
foreground.thumbnail(size)
backgroundColor = backgroundGey.convert(mode="RGB", matrix=None, dither=None, palette=0, colors=0)
backgroundColor.paste(foreground, (0, 505), foreground)
backgroundColor.save("result_hero.png", "PNG")