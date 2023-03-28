from PIL import Image

#tables for later on
ColorTable = []

#function for generating
def colorGen(x, y):
    index = (y*width)+x
    return ColorTable[index][1]

img = Image.open("img.jpg")
width, height = img.size

#scan through pixels (top to bottom, left to right)
for y in range(height):
    for x in range(width):
        if not x+1 > width-1:
            r, g, b, a = img.getpixel((x, y))
            nr, ng, nb, na = img.getpixel((x+1, y))#next red, next green, ...
            #print(f"Pixel ({x}, {y}): RGB = ({r, g, b})")
            ColorTable.append([(r, g, b), (nr, ng, nb)])
        else:
            r, g, b, a = img.getpixel((x, y))
            nr, ng, nb, na = img.getpixel((x, y))#next red, next green, ...
            #print(f"Pixel ({x}, {y}): RGB = ({r, g, b})")
            ColorTable.append([(r, g, b), (nr, ng, nb)])
            
print("Done")

newImage = Image.new("RGB", (width, height))

# if input("Generate Plain Image for you to color? (y/n): ") != "n":
#     print("Generated Plain Image")
#     if input("Are you done cololring it? (y/n): ") != "n":
#         print("Too lazy to do this stuff now haha")
# else:

#make the image completely white first, to check what has to be colored
for y in range(height):
    for x in range(width):
        newImage.putpixel((x, y), (255, 255, 255))

newImage.save("newImg.jpg")
#we'll do customization later on here
newImage = Image.open("newImage.jpg")

#set first pixel to something random from the original image
newImage.putpixel((0, 0), (colorGen(width-1, height-1)))

for y in range(height):
    for x in range(width):
        cr, cg, cb = newImage.getpixel((x, y)) #current red, current blue, ...
        if cr == 255 and cg == 255 and cb == 255:
            r, g, b = colorGen(x, y)
            newImage.putpixel((x, y), (r, g, b))

newImage.save("newImg.jpg")