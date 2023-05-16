from PIL import Image, ImageFilter

def lab71():

    image = Image.open("1.png")
    image.show()

    print( image.format, image.size, image.mode)


def lab72():
    image = Image.open("2.jpg")

    image2 = image
    newW = image.size[0]
    newH = image.size[1]
    image2 = image2.resize([newW,newH])
    image2.save("2um.jpg")

    image3 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image3.save("2zerk.jpg")

    image4 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image4.save("2zerk2.jpg")


def lab73():
    spisok = ["1.png","2.jpg","3.png","4.jpg","5.png"]

    for i in spisok:
        image = Image.open(i)

        image = image.filter(ImageFilter.CONTOUR)
        image.show()


def lab74():

    image = Image.open("2.jpg")
    Mark = Image.open("6.jpg")


    Mark = Mark.resize([100,100])
    image.paste(Mark, [100,100], mask=Mark)
    image.show()
