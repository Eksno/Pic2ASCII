from PIL import Image
import numpy as np
import sys
import os


def main():
    maxValue = 255

    if len(sys.argv) > 1:
        size_multiplier = float(sys.argv[1])
    else:
        size_multiplier = 0.33

    if len(sys.argv) > 2:
        asciiBig2Small = [arg for arg in sys.argv[2:]]
        asciiBig2Small.append(" ")
    else:
        asciiBig2Small = ["w", "#", "+", "-", " "]

    path = os.path.dirname(os.path.abspath(__file__)) + "\\pictures\\"  # Gets the path

    with os.scandir(path) as dir:
        for picture_name in dir:
            picture_name = picture_name.name
            pillow_img = Image.open(path + picture_name).convert('L')  # Gets the image and converts it to gray scale

            width, height = pillow_img.size  # Gets width and height

            pillow_img = pillow_img.resize((
                round(width * size_multiplier),
                round(height * size_multiplier * 0.5)  # Multiplied with 0.5 because of the size of ascii characters.
            ))

            img = np.array(pillow_img)

            ascii_art = create_ascii_art(pillow_img.size[0], pillow_img.size[1], img, asciiBig2Small)
            create_and_write_to_txt_file(ascii_art, picture_name + ".txt")


def create_ascii_art(width, height, image, characters):
    increment_value = (len(characters) - 1) / 255

    ascii_art = []
    for y in range(height):
        ascii_art.append("\n")
        for x in range(width):
            ascii_art.append(characters[int(round(image[y][x] * increment_value))])

    return ''.join(ascii_art)


def create_and_write_to_txt_file(ascii_art, file_name):
    print("writing image", file_name)

    with(open(os.path.dirname(os.path.abspath(__file__)) + "\\output\\" + file_name, "w+")) as f:
        f.write(ascii_art)
        f.close()


if __name__ == "__main__":
    main()
