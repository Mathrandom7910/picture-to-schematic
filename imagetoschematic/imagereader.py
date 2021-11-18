from PIL import Image as Img
from nbtschematic import SchematicFile
from getbrightnessval import get_bright


def get_image_pixels(path, dark, light):
    try:
        im = Img.open(path)
    except:
        print("unable to get image file")
    size = im.size
    sizex = size[0]
    sizey = size[1]
    pix = im.load()
    sf = SchematicFile(shape=(1, sizey, sizex))

    for i in range(sizex):
        for j in range(sizey):
            pin = pix[i, j]
            if get_bright(pin[0], pin[1], pin[2]) < (256 / 2):
                sf.blocks[0, j, i] = dark
                print("set block " + str(i) + " 1 " + str(j) + " to dark block")
            else:
                if not True:
                    sf.blocks[0, j, i] = light
                print("set block " + str(i) + " 1 " + str(j) + " to light block")
    return sf
