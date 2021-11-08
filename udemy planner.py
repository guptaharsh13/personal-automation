import os
from pathlib import Path
import cv2
import mimetypes

path = input('Enter absolute path to your udemy course folder - ')
path = fr'{path}'.format(path=path)

def getVideoLength(video_path):

    video = cv2.VideoCapture(video_path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    return float(frames / fps)

content = []

def searchFolder(path):
    global content
    os.chdir(path)
    count = 0
    sec = 0
    for dir in sorted(os.listdir()):
        
        dir_name = os.path.join(os.getcwd(), dir)
        
        if os.path.isdir(dir):
            dir_info = searchFolder(dir_name)

            hours = int(dir_info[0]/3600)
            minutes = int((dir_info[0]/60)%60)
            content.append(f'{dir}\nNumber of Videos - {dir_info[1]}\nTime required to complete the module - {hours} hour {minutes} minutes\n\n')

            os.chdir(Path(os.getcwd()).parent)
            
        if mimetypes.guess_type(dir_name)[0] and mimetypes.guess_type(dir_name)[0].startswith('video'):
            count += 1
            sec += getVideoLength(dir_name)
            
    return [sec, count]

temp = os.getcwd()
searchFolder(path)

content.sort()
content = '\n'.join(content)

plan = open(os.path.join(temp, "course plan.txt"), 'a')
plan.write(content)
plan.close()