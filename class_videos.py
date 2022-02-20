import cv2
from PIL import Image
from pytesseract import pytesseract
import re
import os
import mimetypes

date_map = {
    "01": "jan",
    "02": "feb",
    "03": "march",
    "04": "apr",
    "05": "may",
    "06": "june",
    "07": "july",
    "08": "aug",
    "09": "sept",
    "10": "oct",
    "11": "nov",
    "12": "dec",
}


def findDate(path):

    # capture image from the video (using image path)

    cam = cv2.VideoCapture(path)
    cam.set(1, 15)
    _, frame = cam.read()
    cv2.imwrite("./temp.jpg", frame)
    cam.release()
    cv2.destroyAllWindows()

    # find text from the image

    image = Image.open("./temp.jpg")
    data = pytesseract.image_to_string(image)[:-1]

    # find the date from data

    temp_date = re.findall(r"(?:.|\n)+(\d{4}-\d{2}-\d{2})(?:.|\n)+", data)[0]
    month = date_map[temp_date.split("-")[1]]
    final_date = int(temp_date.split("-")[-1])
    f_name = f"{month} {final_date}.mp4"
    return f_name


def main():
    path = input('Enter absolute path to your course folder - ')
    path = fr'{path}'.format(path=path)
    os.chdir(path=path)

    names = []

    for video in os.listdir():

        video_path = os.path.join(os.getcwd(), video)

        if not mimetypes.guess_type(video_path)[0] and mimetypes.guess_type(video_path)[0].startswith('video'):
            continue

        video_date = findDate(video_path)
        if video_date in names:
            video_date = video_date.split(".")[0]
            if "|" in video_date:
                temp = int(video_date.split("|")[-1].strip()) + 1
                video_date = f"{video_date.split('|')[0].strip()} {temp}.mp4"
            else:
                video_date = f"{video_date} | 2.mp4"
        names.append(video_date)
        os.rename(video_path, os.path.join(os.getcwd(), video_date))

    os.remove(os.path.join(os.getcwd(), "temp.jpg"))


if __name__ == "__main__":
    main()
