import cv2
import os
import sys
import time


def getSettings():
    shading_1 = " .:-=+*#%@"
    shading_2 = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    shading_3 = " ░▒▓█"
    shading = shading_1
    resolution = (237, 67)
    path = 'video.png'
    tick = 10

    argv = sys.argv[1:]
    if not all("=" in arg for arg in argv):
        return [argv]

    arg_dict = {arg.split("=")[0]: arg.split("=")[1] for arg in argv}

    if "s" in arg_dict:
        if arg_dict["s"] == "1":
            shading = shading_1
        elif arg_dict["s"] == "2":
            shading = shading_2
        else:
            shading = shading_3
    if "w" in arg_dict:
        resolution = (int(arg_dict["w"]), resolution[1])
    if "h" in arg_dict:
        resolution = (resolution[0], int(arg_dict["h"]))
    if "p" in arg_dict:
        path = arg_dict["p"]
    if "t" in arg_dict:
        tick = int(arg_dict["t"])

    return shading, resolution, path, tick


def loadVideo(path):
    video = cv2.VideoCapture(path)
    images = []

    while True:
        a = video.read()
        if not a[0]:
            break
        images.append(a[1])

    return images


def loadImage(image, resolution):
    return cv2.cvtColor(cv2.resize(image, resolution), cv2.COLOR_BGR2GRAY)


def transform(image, shading):
    return "\n".join(["".join([shading[(round((pixel * (len(shading) - 1)) / 256))] for pixel in list(row)]) for row in list(image)])


def display(asc):
    os.system('cls')
    print(asc, end="")


def main():
    response = getSettings()
    if len(response) == 1:
        print(response)
        return None
    else:
        shading, resolution, path, tick = response

    images = loadVideo(path)
    for image in images:
        image = loadImage(image, resolution)
        asc = transform(image, shading)
        display(asc)
        time.sleep(tick/1000)
    input()


if __name__ == '__main__':
    main()
