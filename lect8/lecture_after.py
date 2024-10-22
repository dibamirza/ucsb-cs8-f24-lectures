# To install PIL, type `pip install pillow` in the console
from PIL import Image

# Open an existing image file
pic = Image.open("butterfly.jpg")
width = pic.size[0]
height = pic.size[1]

# Creating a new Canvas
new_pic = Image.new("RGB", (width, height), (0, 0, 0))

pix = pic.getpixel((0,0))
print(pix)
for x in range(width):
    color = pic.getpixel((x, 0))
    for y in range(height):
        new_pic.putpixel((x, y), color)
    print(color)
new_pic.save("new_image1.jpg")

for y in range(height):
    color = pic.getpixel((0, y))
    for x in range(500):
        new_pic.putpixel((x, y ), color)

new_pic.save("new_image3.jpg")

for x in range(width):
    for y in range(500):
        color = pic.getpixel((0, y))
        new_pic.putpixel((x, y ), color)

new_pic.save("new_image2.jpg")


# gray scale effects

new_pic2 = Image.new("RGB", (width, height), (0, 0, 0))
for x in range(width):
    for y in range(height):
        color = pic.getpixel((x, y))
        new_color = (color[0], color[0], color[0])
        new_color = (int(sum(color) / 3),) * 3 # (100,)
        new_pic2.putpixel((x, y ), new_color)


new_pic2.save("graybutterfly.jpg")



# Write a line of code to get the dimensions of the image



# Write code to manipulate pic

# Save the modified image to a new file
pic.save("mybutterfly.jpg")

# Run your code 
# see the new file appear on the left panel under "Files"
