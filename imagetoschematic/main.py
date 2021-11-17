from imagereader import get_image_pixels

imgpath = ""
img_out_path = ""
#49 is obby
dark_block_id = -1
#0 is air
light_block_id = -1


def main(img_path, img_output_path, dbid, lbid):
    image_path = img_path
    if img_path == "":
        image_path = input("Image path?")

    if img_output_path == "":
        img_output_path = input("Result path (include FULL file name, including .schematic extension)?")

    if dbid == -1:
        dbid = int(input("dark block (number only) id, 49 is obsidian"))

    if lbid == -1:
        lbid = int(input("light block (number only) id, 0 is air"))

    schema = get_image_pixels(image_path, dbid, lbid)
    schema.save(img_output_path)
    return


if __name__ == "__main__":
    main(imgpath, img_out_path, dark_block_id, light_block_id)
