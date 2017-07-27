from PIL import Image,ImageDraw,ImageFont

imageFile = "0001.jpg"
im = Image.open(imageFile)
im = im.transpose(Image.ROTATE_270)

print(im.format, im.size, im.mode)

xsize,ysize = im.size

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf",100)

draw.text((758,365),"jfiejwfofjewf", fill = (128, 0, 128),font=font)
# draw.text((0, 0),"1",(255,255,0))
del draw

im = im.transpose(Image.ROTATE_90)
im.show()

# im.save("target.jpg")