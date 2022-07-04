from PIL import Image, ImageFont, ImageDraw

im = Image.new('1', (800, 480), (1))
#img = Image.open("sample_in.jpg")
draw = ImageDraw.Draw(im)

### ### ### LINE

luft = 50

# draw.line(x1,y1,x2,y2)
draw.line((0+luft, 240, 800-luft, 240), fill=(0), width=(5))
draw.line((400, 0+luft, 400, 480-luft), fill=(0), width=(5))
draw.line((200, 0+luft, 200, 480-luft), fill=(0), width=(5))
draw.line((600, 0+luft, 600, 480-luft), fill=(0), width=(5))
# draw.ellipse((100, 100, 150, 200), fill=(0), outline=(1))
# draw.rectangle((200, 100, 300, 200), fill=(0), outline=(1))
# draw.line((350, 200, 450, 100), fill=(0), width=(10))

### ### ### TEXT

# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("sans-serif.ttf", 12)
font = ImageFont.load_default()
font2 = ImageFont.truetype("Helvetica.tff", 12, encoding="unic")

# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((50, 50),'Velkommen til Tavlen',(0),font=font)
draw.text((200+20, 50),'Her kan det stå masse',(0),font=font)
draw.text((200*2+20, 50),'Det er bra',(0),font=font)
draw.text((200*2+20, 200+50),'Her kan det stå ting også',(0),font=font2)

### ### ### PRODUCE

#img.save('sample-out.jpg')
im.save('pillow_imagedraw4.bmp', quality=95)







# ImageDraw.Draw(
#     im  # Image
# ).text(
#     (0, 0),  # Coordinates
#     'Hello world!',  # Text
#     (0)  # Color
# )
