import os
from pathlib import Path
from utils import lenVideo, isVideo, convertTime

path = input('Enter the absolute path to your udemy course folder - ')
path = fr'{path}'.format(path=path)


modules = []
total_time = 0


def searchFolder(path):
    global content
    global total_time
    os.chdir(path)
    count = 0
    seconds = 0
    for file in os.listdir():

        absolute_path = os.path.join(os.getcwd(), file)

        if os.path.isdir(file):
            seconds, count = searchFolder(absolute_path)

            modules.append({
                "module_name": file,
                "number_of_videos": count,
                "time_required": seconds

            })

            total_time += seconds

            os.chdir(Path(os.getcwd()).parent)

        if isVideo(absolute_path):
            count += 1
            seconds += lenVideo(absolute_path)

    return seconds, count


searchFolder(path)
modules.sort(key=lambda module: int(module.get("module_name").split(".")[0]))


def mapContent(module):
    return f'{module.get("module_name")}\nNumber of Videos - {module.get("number_of_videos")}\nTime required to complete the module - {convertTime(module.get("time_required"))}\n\n'


content = '\n'.join(map(mapContent, modules))

content = f'Time required to complete the entire course = {convertTime(total_time)}.\n\n{content}'

with open(os.path.join(path, "course plan.txt"), "w") as plan:
    plan.write(content)
