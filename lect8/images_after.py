# Lecture 8: Images and Loops
from PIL import Image

# open an existing image
pic = Image.open("butterfly.jpg")
pic.show()
width = pic.size[0]
height = pic.size[1]

 
new_pic = Image.new('RGB', (width, height), (0, 0, 0))
##new_pic.show()

## Get all the pixels in the first row of butterfly

for x in range(width):
    color = pic.getpixel((x, 0))
    for y in range(height):
        new_pic.putpixel((x, y), color)
    print(color)


### Smear the pixels of the butterfly horizontally

for y in range(height):
    color = pic.getpixel((0, y))
    for x in range(width):
        new_pic.putpixel((x, y), color)



for x in range(width):
    for y in range(height):
        color = pic.getpixel((x, y))
        new_color = (int(sum(color) / 3), ) * 3
        new_pic.putpixel((x, y), new_color)

new_pic.show()

        
        

new_pic.save("mycanvas.jpg")
