from imagereader import get_image_pixels
from launchgui import gui_launch
import time
import os


def main(img_path, img_output_path, dbid, lbid):
    if img_path == "":
        input("Cannot use invalid path!")
    image_path = img_path

    if os.path.exists(img_output_path):
        if input("File already occupied, overwrite? Y/N").lower() == "y":
            os.remove(img_output_path)
        else:
            print("Please choose different path")
            return


    schema = get_image_pixels(image_path, dbid, lbid)
    try:
        schema.save(img_output_path)
    except:
        print("unable to write to path")
    return


if __name__ == "__main__":
    main(*gui_launch())
