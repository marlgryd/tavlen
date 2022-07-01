from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
draw=Drawing()

### SET VARS
mystepvalue = 15

with Image(filename='empty.bmp') as image:
          print(image.size)
          image.antialias = False
          draw.stroke_width = 1
          draw.stroke_color = Color('black')
          draw.fill_color = Color('black')
          #
          # --- draw the lines ---
          #
          for xpos in range(0,4790,mystepvalue):
                    draw.line( (xpos,0), (xpos, image.height) )

          draw(image)  # Have to remember this to see anything...

          # # None of this makes a 2bit BMP
          # image.depth = 2
          # image.colorspace = "gray"
          # image.antialias = False
          # image.monochrome = True
          # image.imagedepth =2
          # image.save(filename='result.bmp')

          image.quantize(2, colorspace_type='gray', dither=True)
          image.depth = 2
          image.colorspace = 'gray'
          image.type = 'bilevel'  # or grayscale would also work.
          image.save(filename='result.bmp')
