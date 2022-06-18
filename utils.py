import cv2
import mimetypes


def convertTime(seconds):
    hours = int(seconds/3600)
    minutes = int((seconds/60) % 60)
    seconds -= hours * 3600 + minutes * 60
    seconds = int(seconds)
    return f'{str(hours) + " hours " if hours else ""}{str(minutes) + " minutes " if minutes else ""}{seconds} seconds'


def isVideo(path):
    return mimetypes.guess_type(path)[0] and mimetypes.guess_type(path)[0].startswith('video')


def lenVideo(path):

    if not isVideo(path=path):
        return 0

    video = cv2.VideoCapture(path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(video.get(cv2.CAP_PROP_FPS))

    return float(frames / fps)
