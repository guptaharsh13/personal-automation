import os
import cv2
import mimetypes

path = input('Enter absolute path to your videos folder - ')
divide_time = int(input("Enter the amount of time / day (in minutes) - "))
divide_time *= 60
path = fr'{path}'.format(path=path)


def findVideoLength(video_path):

    video = cv2.VideoCapture(video_path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(video.get(cv2.CAP_PROP_FPS))

    return float(frames / fps)


# plan_f = open("plan.txt", "w")
# plan_f.write("Aim / Plan\n")

os.chdir(path=path)
seconds = 0
temp_seconds = 0
count = 1
# plan_f.write(f"\n\nDay {count}\n\n")

# custom code


def myFunc(f_name):
    if "lesson" in f_name:
        return int(f_name[6:-4])
    return -1


files = os.listdir()
# files.sort(key=myFunc)

for video in files:
    video_path = os.path.join(os.getcwd(), video)
    if mimetypes.guess_type(video_path)[0] and mimetypes.guess_type(video_path)[0].startswith('video'):
        seconds += findVideoLength(video_path=video_path)
        temp_seconds += findVideoLength(video_path=video_path)

        # plan_f.write(f"{video}\n")

        # if temp_seconds >= divide_time:
        #     count += 1
        #     temp_seconds = 0
        #     plan_f.write(f"\n\nDay {count}\n\n")


def calcTime(seconds):
    hours = int(seconds/3600)
    minutes = int((seconds/60) % 60)
    return (hours, minutes)


print(
    f"\nTime required at normal speed = {calcTime(seconds=seconds)[0]} hours and {calcTime(seconds=seconds)[1]} minutes")
seconds /= 1.25
print(
    f"\nTime required at 1.25X speed = {calcTime(seconds=seconds)[0]} hours and {calcTime(seconds=seconds)[1]} minutes")
seconds = seconds*1.25/1.5
print(
    f"\nTime required at 1.5X speed = {calcTime(seconds=seconds)[0]} hours and {calcTime(seconds=seconds)[1]} minutes")
seconds = seconds*1.5/1.75
print(
    f"\nTime required at 1.75X speed = {calcTime(seconds=seconds)[0]} hours and {calcTime(seconds=seconds)[1]} minutes")
seconds = seconds*1.75/2
print(
    f"\nTime required at 2X speed = {calcTime(seconds=seconds)[0]} hours and {calcTime(seconds=seconds)[1]} minutes")
print("\nYour plan has been created. Check plan.txt !!")

# plan_f.close()
