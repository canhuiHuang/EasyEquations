from PIL import Image

background = Image.open("test1.png")
foreground = Image.open("test2.jpg")
foreground = foreground.convert('RGBA')

background.paste(foreground, (0, 0), foreground)
background.show()