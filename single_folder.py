import os
from utils import convertTime, lenVideo, isVideo

path = input('Enter the absolute path to your videos folder - ')
path = fr'{path}'.format(path=path)


os.chdir(path=path)
seconds = 0


files = os.listdir()

for file in files:
    absolute_path = os.path.join(os.getcwd(), file)
    seconds += lenVideo(path=absolute_path)

speeds = [1, 1.25, 1.5, 1.75, 2, 2.5, 2.7, 3, 3.25, 3.5]

for speed in speeds:
    seconds /= speed
    print(
        f"\nTime required at a speed of {speed}x - {convertTime(seconds=seconds)}")
    seconds *= speed
