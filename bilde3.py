from PIL import Image, ImageDraw

im = Image.new('1', (800, 480), (1))
draw = ImageDraw.Draw(im)

draw.ellipse((100, 100, 150, 200), fill=(0), outline=(1))
draw.rectangle((200, 100, 300, 200), fill=(0), outline=(1))
draw.line((350, 200, 450, 100), fill=(0), width=10)

im.save('pillow_imagedraw3.bmp', quality=95)
